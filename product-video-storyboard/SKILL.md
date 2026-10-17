---
name: product-video-storyboard
description: Turn an approved product-video script plus a product image or readable product link into FULL single-paragraph English video prompts and six-panel portrait image storyboards, in SINGLE mode (1 storyboard + 1 prompt) or SPLIT mode (clip A hook + clip B product, 2 storyboards + 2 prompts, merged A then B). Includes the hook formula, an audio and language lock, and post-production edit rules and scripts for short product sales videos. Use for storyboard/prompt kits for Flow, Veo, Seedance or similar reference-video tools, including targeted revisions. Not for rendering videos, channel scraping or inventing sales scripts without approval.
---

# Product Video Storyboard (v2)

## IMPORTANT NOTICE: create your OWN AI characters

This skill ships NO characters, cast sheets or identities. Before any storyboard is made, the user must create (or approve) their own original AI characters. Never reuse, recreate or "continue" characters from anywhere else: not from memory or notes, not from earlier projects or chats, not from another person's channel, not from example prompts in this repository. If the environment contains saved character descriptions, ignore them unless the user explicitly says they are theirs and approved for this run. Examples in this skill use neutral placeholders such as `[HERO]` and `[PARTNER]` on purpose.

Show this notice to the user at the start of a new kit, in their language. Vietnamese version: "Lưu ý quan trọng: hãy tự tạo nhân vật AI của riêng bạn. Skill này không kèm nhân vật nào và không được dùng lại nhân vật của kênh khác, của dự án cũ hay trong bộ nhớ. Hãy tạo một bảng nhân vật (cast sheet), duyệt nó, rồi mới làm storyboard." Details: [references/characters.md](references/characters.md).

## What this skill produces

Deliver matching `prompt.txt` and `sb.png` files, not a video. Communicate in the user's language. Default format: 10-second 9:16 clip and a portrait 2:3 board with six equal panels, two columns by three rows, read left-to-right then top-to-bottom. User choices override defaults.

## Choose the mode: 1 storyboard or 2 storyboards

Typical sales videos follow the HOOK FORMULA: a hook that grabs attention and creates curiosity, then a product reveal (unboxing), then use or demonstration, then a check-in or call to action. See [references/hooks.md](references/hooks.md). Pick the mode before writing anything.

| Use SINGLE mode (1 SB + 1 prompt, one clip) when | Use SPLIT mode (2 SB + 2 prompts, clips A and B) when |
|---|---|
| Everything happens in one location and one continuous scene | The story changes location or time (for example shop then home) |
| The hook has no physical event that changes object state | The hook contains a physical event: drop, spill, fall, topple, break |
| Six or fewer distinct beats fit the duration | More than six beats, or the hook and product need separate controls |
| The product appears from the first second (demo, use, reaction) | A single-storyboard attempt already failed on the hook (object already fallen, floating, wrong order) |
| You do not plan to test different hooks | You want to reuse a hook with several products, or test several hooks for one product |

Rule of thumb: if the hook needs a "before then after" object state, or the scene cuts to another place, split. Otherwise stay single. SPLIT costs two generations plus a merge; say so to the user. Explain the choice in one or two sentences before producing files.

- SINGLE mode: follow [references/templates.md](references/templates.md) section "Single clip".
- SPLIT mode: follow "Split clips A and B" in the same file and [references/hooks.md](references/hooks.md). Clip B must attach clip A's storyboard (or the cast sheet) as the identity reference.

## Required reading

For a new kit or revision, read [references/workflow.md](references/workflow.md), [references/templates.md](references/templates.md), [references/hooks.md](references/hooks.md), [references/characters.md](references/characters.md) and [references/qa.md](references/qa.md). For editing the finished videos read [references/edit-post.md](references/edit-post.md). Use [references/claude-project.md](references/claude-project.md) only for the Claude Project fallback. Follow any applicable image-generation skill provided by the current environment before generating images.

## Input and evidence gate

Require an approved script, an approved cast sheet (see the notice above) and a product image actually viewed. A product link substitutes only when its exact product images can be opened and visually inspected; page text alone is insufficient. If blocked, ask the user for a clear front-facing product photo and stop product-locked final generation; preliminary shot planning may be clearly marked provisional. Resolve conflicts between link and photo with the user.

Preserve the approved story, hook, characters, artwork, actions and CTA. Add filming mechanics, not new plot. A pet/person in printed artwork is not a live scene character. Never infer invisible construction, health results, gift packaging or free personalization claims.

## Audio and language lock (mandatory in every video prompt)

Video tools fill silence with speech in their default language. In a real test, a clip generated from a prompt that said "no spoken dialogue" still had a character speaking Mandarin (confirmed by transcription). "No dialogue" alone is therefore NOT enough. Every video prompt, including product-only shots, must contain an explicit audio and language lock:

1. Default (the approved script has no exact spoken line): write a NO-SPEECH lock, for example: `Audio: [AMBIENCE AND SFX]. Nobody speaks: mouths stay closed or move only in natural non-verbal reactions (smile, gasp, laugh, breath); no lip-synced speech, narration or singing in any language, in particular no Chinese or Mandarin voices; no added music unless approved.`
2. If the approved script has an exact spoken line: write a dialogue lock in the language you want, for example: `Dialogue (American English only, never Chinese or any other language): [SPEAKER] says exactly "[LINE]" at [T1]-[T2]s in a natural American [MALE/FEMALE] voice with synchronized lips; no other speech.` Never leave the language to the tool's default.
3. Always add to the Avoid list: Chinese or Mandarin speech, any non-English speech, unrequested speech or narration, model-generated subtitles. (If your target language is not English, adapt the lock but keep it explicit.)
4. After the real video exists, run the audio language check in [references/qa.md](references/qa.md) (`scripts/edit/check_audio_language.py`). If speech in the wrong language appears, tighten the lock and regenerate, or use the voice-replacement fallback in [references/edit-post.md](references/edit-post.md).

## Process

1. Show the character notice. Confirm an approved cast sheet exists; if not, help the user create one first (references/characters.md).
2. Establish verified product invariants, approved identities, setting and spatial layout. Read the script rather than borrowing details from examples. If adapting a source video, inspect it first and obtain approval for the adapted script before producing final assets.
3. Choose SINGLE or SPLIT mode with the table above and tell the user why.
4. Map the approved actions to chronological keyframes and feasible time intervals; panels do not imply equal-duration shots. In SPLIT mode, divide the story at the natural cut (usually hook, then product) and give each clip its own six keyframes. If the duration cannot support the actions, ask before shortening the story or extending duration.
5. Produce each board with a real raster image-generation/editing tool using actual product and identity attachments. Inspect it panel by panel, correct targeted errors, and keep the prompt aligned. A written filename is not an uploaded reference. For a hook with a physical event, panel 1 must show the START state, never the end state.
6. Write a FULL English prompt per clip, one paragraph with no embedded newlines, following the templates and including the audio and language lock. Bind tags to actual attachment names. Explicitly distinguish continuous motion from cuts, printed artwork from overlays, and board layout from full-screen video.
7. Apply the QA checklist and `scripts/check.py`. The script checks technical invariants only; visually verify panel count, product and story separately.
8. Deliver only files that exist, report text-only or unresolved items truthfully, and state what has not been tested. Do not install/publish/upload/render unless separately authorized.

## Tools and output boundaries

This skill contains no image or video model, credentials, scraping integration or upload integration. Use available authorized tools; never replace missing image generation with a fake PNG path, placeholder SVG, or claims of successful rendering. Without image generation, deliver `prompt.txt`, `img.txt` and the six-keyframe specification with an explicit statement that the storyboard PNG has not been generated. Without verified product imagery, stop before final product-locked outputs instead.

Output layout: SINGLE mode writes `prompt.txt` and `sb.png` in the project folder. SPLIT mode writes the same two files in subfolders `a/` and `b/` (names and tags `<code>_a`, `<code>_b`) plus a short `note.md` giving the merge order and cut point. Follow the user's own folder and naming conventions when supplied. Keep old revisions; no default ZIP.

Never assume @tags, duration, audio, text rendering or reference modes work identically across applications. Ask the actual model/mode when troubleshooting; do not shorten prompts or bypass safety restrictions as a speculative fix.

## Post-production scripts (optional)

`scripts/edit/` holds small helpers for the finished clips: build a text-overlay edit project, replace a wrongly spoken voice while keeping the music, and check the spoken language of an MP4. They are optional, need external tools (ffmpeg, HyperFrames, Demucs, a TTS engine, faster-whisper) and are explained in [references/edit-post.md](references/edit-post.md). The skill itself never renders or posts anything.
