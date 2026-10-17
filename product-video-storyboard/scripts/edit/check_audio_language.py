#!/usr/bin/env python3
"""Transcribe the audio of a finished clip and report the spoken language.

Usage:
  python check_audio_language.py clip.mp4 --expect none     # clip must have NO speech (music/ambience only)
  python check_audio_language.py clip.mp4 --expect en       # clip must contain speech in English
  python check_audio_language.py clip.mp4                   # just report

Requires: ffmpeg on PATH and `pip install faster-whisper` (downloads a small speech model on first run).
Heuristic only: speech models can hallucinate words on music, so for --expect none a clip is flagged only when
confident speech is found. Always confirm borderline results by listening. Exit code 1 = check failed.
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('video')
    ap.add_argument('--expect', default=None, help='none, or a language code such as en')
    ap.add_argument('--model', default='small')
    args = ap.parse_args()

    from faster_whisper import WhisperModel
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / 'a.wav'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', args.video, '-vn', '-ac', '1', '-ar', '16000', str(wav)], check=True)
        model = WhisperModel(args.model, device='cpu', compute_type='int8')
        segments, info = model.transcribe(str(wav), beam_size=5)
        segs = list(segments)
    print(f'detected language: {info.language} (confidence {info.language_probability:.2f})')
    speech = [s for s in segs if s.no_speech_prob < 0.5 and s.avg_logprob > -1.0 and len(s.text.strip()) > 2]
    for s in segs:
        flag = 'speech' if s in speech else 'weak'
        print(f'  {s.start:6.2f}-{s.end:6.2f} [{flag}] {s.text.strip()}')

    if args.expect is None:
        return 0
    if args.expect == 'none':
        if speech and info.language_probability >= 0.6:
            print('FAIL: speech found in a clip that must have none')
            return 1
        print('PASS: no confident speech found')
        return 0
    if not speech:
        print(f'FAIL: expected {args.expect} speech, none found')
        return 1
    if info.language != args.expect:
        print(f'FAIL: expected language {args.expect}, detected {info.language}')
        return 1
    print(f'PASS: speech detected in {args.expect}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
