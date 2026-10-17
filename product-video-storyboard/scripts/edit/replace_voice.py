#!/usr/bin/env python3
"""Replace a wrongly spoken voice in a finished clip with a synthesized voice, keeping the music.

Usage:
  python replace_voice.py --video clip.mp4 --parts parts.json --out-audio fixed_audio.wav [--mux fixed.mp4] [--voice en-US-AndrewNeural]

parts.json: the corrected lines with where they should start in the clip (seconds) and the latest end time:
  [{"text": "Don't worry.", "start": 3.6, "max_end": 4.45, "rate": "+0%"},
   {"text": "I've got something better for you.", "start": 5.25, "max_end": 6.75, "rate": "+12%"}]
Find the original speech window first (for example with check_audio_language.py or any transcriber).

Steps: extract audio -> Demucs separates vocals from music -> keep the music ("no_vocals") stem ->
synthesize each part with edge-tts -> time and mix -> optionally mux into the video without re-encoding the picture.
Requires: ffmpeg, `pip install demucs edge-tts torch torchaudio` (a virtual environment with a SHORT path is advised on
Windows). Limits: lip movement still follows the original language, and the synthesized voice is not a real actor.
If speech is prominent on screen, regenerating the clip with a stronger audio lock is usually better.
Always verify the result with check_audio_language.py --expect en.
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def duration(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(path)]).decode().strip())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--video', required=True)
    ap.add_argument('--parts', required=True)
    ap.add_argument('--out-audio', required=True)
    ap.add_argument('--mux', default=None)
    ap.add_argument('--voice', default='en-US-AndrewNeural')
    ap.add_argument('--work', default=None, help='working folder (default: a temporary folder)')
    args = ap.parse_args()
    parts = json.loads(Path(args.parts).read_text(encoding='utf-8'))

    tmp = None
    if args.work:
        work = Path(args.work)
        work.mkdir(parents=True, exist_ok=True)
    else:
        tmp = tempfile.TemporaryDirectory()
        work = Path(tmp.name)

    audio44 = work / 'audio44.wav'
    run(['ffmpeg', '-v', 'error', '-y', '-i', args.video, '-vn', '-ac', '2', '-ar', '44100', str(audio44)])
    run([sys.executable, '-m', 'demucs.separate', '-n', 'htdemucs', '--two-stems=vocals', '-o', str(work / 'stems'), str(audio44)])
    music = work / 'stems' / 'htdemucs' / 'audio44' / 'no_vocals.wav'
    if not music.is_file():
        raise SystemExit('Demucs output not found: ' + str(music))

    inputs = ['-i', str(music)]
    filters, labels = [], ['[0:a]']
    for i, p in enumerate(parts, start=1):
        mp3 = work / f'part{i}.mp3'
        run([sys.executable, '-m', 'edge_tts', '--voice', args.voice, f'--rate={p.get("rate", "+0%")}', '--text', p['text'], '--write-media', str(mp3)])
        wav = work / f'part{i}.wav'
        run(['ffmpeg', '-v', 'error', '-y', '-i', str(mp3), '-af',
             'silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=1:stop_threshold=-45dB:stop_duration=0.15',
             '-ar', '44100', '-ac', '2', str(wav)])
        d = duration(wav)
        window = p['max_end'] - p['start']
        tempo = min(1.25, d / window) if d > window else 1.0
        ms = int(p['start'] * 1000)
        filters.append(f'[{i}:a]atempo={tempo:.3f},loudnorm=I=-17:TP=-2:LRA=7,adelay={ms}|{ms}[v{i}]')
        labels.append(f'[v{i}]')
        inputs += ['-i', str(wav)]
        print(f'part {i}: "{p["text"]}" {d:.2f}s at {p["start"]}s, tempo {tempo:.2f}')
    mix = ';'.join(filters) + ';' + ''.join(labels) + f'amix=inputs={len(labels)}:normalize=0:duration=first,alimiter=limit=0.95[out]'
    run(['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', mix, '-map', '[out]', '-ar', '48000', '-ac', '2', args.out_audio])
    print('audio written:', args.out_audio)
    if args.mux:
        run(['ffmpeg', '-v', 'error', '-y', '-i', args.video, '-i', args.out_audio, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-shortest', args.mux])
        print('muxed video written:', args.mux)
    if tmp:
        tmp.cleanup()


if __name__ == '__main__':
    main()
