# Product Video Storyboard v2 (Codex, Claude Code, Claude Projects)

Skill that turns an **approved product-video script + product image/link** into FULL one-paragraph English video prompts and portrait six-panel storyboards, for tools such as Google Flow/Veo and Seedance. It also covers the finishing steps for short sales videos (text overlays, audio and language checks). It never renders videos, posts, scrapes or uploads by itself.

Skill này biến **kịch bản đã duyệt + ảnh/link sản phẩm** thành prompt video tiếng Anh một đoạn và storyboard ảnh dọc 6 ô, kèm hướng dẫn edit video bán hàng ngắn.

## IMPORTANT: create your OWN AI characters / Hãy tự tạo nhân vật AI của riêng bạn

This repository ships **no characters** and must never be used to recreate another creator's characters (not from memory, not from old projects, not from this repo's examples). Make your own cast sheet, approve it, then build storyboards. Placeholders like `[HERO]` are intentional.

Repo này **không kèm nhân vật nào**. Không dùng lại nhân vật của kênh khác, của dự án cũ hay trong bộ nhớ. Hãy tạo bảng nhân vật (cast sheet) của riêng bạn, duyệt, rồi mới làm storyboard. Chi tiết: `product-video-storyboard/references/characters.md`.

## What is new in v2 / Có gì mới

1. **Two modes: 1 storyboard or 2 storyboards.** Sales videos follow a formula: *hook that grabs attention and creates curiosity, then product reveal (unboxing), then use, then check-in / CTA*.
   - **SINGLE** (1 SB + 1 prompt): one location, one continuous scene, no object event in the hook, six or fewer beats.
   - **SPLIT** (2 SB + 2 prompts, clip A = hook, clip B = product, merged A then B with a hard cut): the scene changes place or time, the hook has a physical event (drop, spill, fall), more than six beats, or a hook already failed in a single board. A hook clip can be reused with several products.
   - Why: a storyboard panel freezes one state. If panel 1 shows the end state of an event (cup already on the floor), the video tool starts there and the event never happens. SPLIT lets clip A start from the START state. See `references/hooks.md`.
2. **Audio and language lock.** "No dialogue" alone is not enough: video tools can invent speech in a default language (a real test produced Mandarin). Every prompt must carry an explicit NO-SPEECH lock or an exact-line, American-English-only dialogue lock, and `scripts/check.py` enforces it.
3. **Post-production** (`references/edit-post.md`, `scripts/edit/`): text overlay rules (hook, middle text, call to action), audio policies, a spoken-language checker (`check_audio_language.py`), a voice replacement fallback that keeps the music (`replace_voice.py`) and a text-overlay project builder (`build_edit.py`).

## Layout

```
product-video-storyboard/
  SKILL.md                      entry point: notice, mode table, audio lock, process
  references/
    workflow.md  templates.md   rules, single and split prompt scaffolds
    hooks.md                    hook formula, physical-event rule, split rules
    characters.md               how to create your own characters
    qa.md                       delivery checklist and audio language check
    edit-post.md                post-production edit guide
    claude-project.md           Claude Project fallback
  scripts/
    check.py                    structural checks (single and split outputs, audio lock)
    edit/                       build_edit.py, check_audio_language.py, replace_voice.py, assets/
test_check.py                   unit tests for check.py
```

## Install

- **Codex terminal:** copy the whole `product-video-storyboard/` folder into `.agents/skills/` of your project, start a session there and call `$product-video-storyboard`. Copy the whole folder, not only SKILL.md.
- **Claude Code:** copy the folder into `.claude/skills/` and call `/product-video-storyboard`.
- **Claude web/Desktop:** custom skills need a ZIP of the skill folder (Customize > Skills). Or add the Markdown files to a Claude Project as knowledge and use `references/claude-project.md` as the project instructions (guidance only).
- The skill needs an environment that can **view images and generate images from references**. Without an image tool it only produces the prompt and an image specification and says the PNG was not generated.

## Typical request

```text
Use product-video-storyboard.
Product: [link or attached photo]
Script: [approved story]
Duration: 10 seconds per clip
Characters: [attach YOUR approved cast sheet]
Audio/text: [requirements, or "no speech"]
Output: prompt + storyboard (the skill chooses SINGLE or SPLIT and explains why)
```

## Check your files

```bash
python product-video-storyboard/scripts/check.py skill product-video-storyboard
python product-video-storyboard/scripts/check.py output <folder>          # prompt.txt + sb.png, or a/ and b/ for SPLIT
python product-video-storyboard/scripts/check.py output <folder> --text-only
python test_check.py
```

`check.py output` verifies files, one-line prompts, unfilled placeholders, PNG header, the audio and language lock and, for SPLIT, the `_a`/`_b` tags and the hard cut. It does NOT prove the product is right, that the board has six panels, or that a video will work. Always inspect the images.

## Third-party assets and licenses

- Code and documents: MIT License (see `LICENSE`).
- `scripts/edit/assets/icon-*.svg` are Twemoji graphics, CC-BY 4.0 (see `LICENSE-icons.txt`). Credit Twemoji when you publish videos that use them.
- External tools (not included): ffmpeg, HyperFrames, Demucs, edge-tts, faster-whisper. Follow their own licenses and terms. edge-tts sends text to an online speech service.

No tokens, customer photos, chat history or third-party reference footage are included.
