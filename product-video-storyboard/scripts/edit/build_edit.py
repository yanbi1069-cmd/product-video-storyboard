#!/usr/bin/env python3
"""Build a HyperFrames project that adds text overlays (hook, middle text, call to action) to a finished clip.

Usage:  python build_edit.py spec.json

The picture and timing of the source clip are never changed (no cuts). The source video is muted inside
the composition; audio is re-added from a separate file so the music/voice is under your control:
  audio.mode = "keep"  -> the original audio is extracted and placed back unchanged
  audio.mode = "file"  -> use your own audio file (a continuous music bed, or a remixed track)
Requires: ffmpeg/ffprobe on PATH. Rendering needs Node.js and HyperFrames:
  cd <out_dir> && npx --yes hyperframes@0.8.160 check && npx --yes hyperframes@0.8.160 render --quality delivery

Example spec.json (all coordinates are in a 1080x1920 canvas, text lines are English):
{
  "source": "clip.mp4",
  "out_dir": "edit_project",
  "hook": {"lines": ["First line", "Second line"], "top": 1500, "start": 0, "duration": 3.5},
  "mid":  {"lines": ["Middle text"], "top": 80, "start": 7.0, "duration": 3.5},
  "cta":  {"lines": ["Make it yours.", "Shop the link in bio."], "top": 110, "start": 17.4},
  "icons": true,
  "audio": {"mode": "keep"}
}
Rules for placement: no background box; high-contrast text with outline; never cover faces, the product or printed lettering;
keep clear of the platform interface margins. Check frames of the real render before delivering.
"""
import html
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def probe_duration(path):
    out = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(path)])
    return round(float(out.decode().strip()), 3)


def block(el_id, tag, cfg, end, size, extra_cls=''):
    lines = ''.join('<span>' + html.escape(x) + '</span>' for x in cfg['lines'])
    dur = cfg.get('duration')
    if dur is None:
        dur = round(end - cfg['start'], 3)
    return (f'<{tag} id="{el_id}" class="clip copy{extra_cls}" style="top:{cfg["top"]}px;font-size:{size}px" '
            f'data-start="{cfg["start"]}" data-duration="{dur}" data-track-index="1">{lines}</{tag}>')


def main(spec_path):
    spec = json.loads(Path(spec_path).read_text(encoding='utf-8'))
    out = Path(spec['out_dir'])
    assets = out / 'assets'
    assets.mkdir(parents=True, exist_ok=True)
    src = assets / 'source.mp4'
    shutil.copy2(spec['source'], src)
    d = probe_duration(src)

    audio = spec.get('audio', {'mode': 'keep'})
    if audio['mode'] == 'keep':
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(src), '-vn', '-ar', '48000', '-ac', '2', str(assets / 'audio.wav')], check=True)
        auto = ''
    elif audio['mode'] == 'file':
        shutil.copy2(audio['file'], assets / 'audio.wav')
        vol = audio.get('volume', 0.45)
        fade = audio.get('fade', 0.8)
        pts = [{'t': 0, 'v': 0}, {'t': 0.15, 'v': vol}, {'t': max(0.2, d - fade), 'v': vol}, {'t': d, 'v': 0}]
        auto = ' data-automation="' + html.escape(json.dumps({'version': 1, 'lanes': [{'target': 'volume', 'points': pts}]}), quote=True) + '"'
    else:
        raise SystemExit('audio.mode must be "keep" or "file"')

    parts = []
    hook = spec.get('hook')
    if hook:
        hook.setdefault('start', 0)
        hook.setdefault('duration', 3.5)
        if spec.get('icons', True):
            for name in ['icon-1f384.svg', 'icon-1f381.svg']:
                shutil.copy2(HERE / 'assets' / name, assets / name)
            top = hook['top'] - 82
            parts.append(f'<img id="tree" class="clip icon" style="top:{top}px;left:468px" src="assets/icon-1f384.svg" alt="" data-start="{hook["start"]}" data-duration="{hook["duration"]}" data-track-index="3">')
            parts.append(f'<img id="gift" class="clip icon" style="top:{top}px;left:548px" src="assets/icon-1f381.svg" alt="" data-start="{hook["start"]}" data-duration="{hook["duration"]}" data-track-index="3">')
        parts.append(block('hook', 'h1', hook, d, 66))
    if spec.get('mid'):
        spec['mid'].setdefault('duration', 3.5)
        parts.append(block('mid', 'h2', spec['mid'], d, 60))
    if spec.get('cta'):
        parts.append(block('cta', 'h2', spec['cta'], d, 65))

    doc = f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080, height=1920"><script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>
*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#191512}}#root{{width:100%;height:100%;position:relative;overflow:hidden}}.footage{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}.copy{{position:absolute;left:100px;right:100px;z-index:4;font-family:Montserrat,Arial,sans-serif;font-weight:700;line-height:1.16;letter-spacing:-1px;text-align:center;color:#fffaf1;-webkit-text-stroke:3.4px #191512;paint-order:stroke fill;text-shadow:0 3px 9px #191512}}.copy span{{display:block}}.icon{{position:absolute;width:60px;height:60px;z-index:4}}
</style></head><body><div id="root" data-composition-id="main" data-start="0" data-duration="{d}" data-width="1080" data-height="1920" data-fps="24">
<video id="footage" class="clip footage" src="assets/source.mp4" playsinline muted data-start="0" data-duration="{d}" data-track-index="0"></video>
{chr(10).join(parts)}
<audio id="track" class="clip" src="assets/audio.wav" data-start="0" data-duration="{d}" data-track-index="2" data-volume="1"{auto}></audio>
</div><script>window.__timelines['main']=gsap.timeline({{paused:true}});</script></body></html>'''
    (out / 'index.html').write_text(doc, encoding='utf-8')
    (out / 'package.json').write_text(json.dumps({'name': out.name, 'private': True, 'type': 'module', 'scripts': {
        'check': 'npx --yes hyperframes@0.8.160 check', 'render': 'npx --yes hyperframes@0.8.160 render --quality delivery'}}, indent=2), encoding='utf-8')
    (out / 'BRIEF.md').write_text(f'---\nworkflow: general-video\nflow: automation\nstoryboard: no\naspect: 1080x1920\ndestination: instagram-reels\nlanguage: en\nlength: {d}s\n---\n'
                                  'Text-overlay edit of a finished clip. Picture and timing unchanged; no cuts. Audio mode: ' + audio['mode'] + '.\n', encoding='utf-8')
    print(f'project written to {out} (duration {d}s)')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
