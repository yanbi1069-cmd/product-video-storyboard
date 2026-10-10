---
name: product-video-storyboard
description: Turn an approved product-video script plus a product image or readable product link into a full single-paragraph English video prompt and a six-panel portrait image storyboard. Use for storyboard/prompt kits for Flow, Veo, Seedance or similar reference-video tools, including targeted revisions. Not for rendering videos, channel scraping or inventing sales scripts without approval.
---

# Product Video Storyboard

Deliver matching `prompt.txt` and `sb.png`, not a video. Communicate in the user's language. The default tested format is a 10-second 9:16 video and a portrait 2:3 board with six equal panels, two columns by three rows, read left-to-right then top-to-bottom. User choices override defaults; eight panels need explicit agreement for difficult actions.

## Required reading

For a new kit or revision, read [references/workflow.md](references/workflow.md), [references/templates.md](references/templates.md) and [references/qa.md](references/qa.md). Use [references/claude-project.md](references/claude-project.md) only for the Claude Project fallback. Follow any applicable image-generation skill provided by the current environment before generating images.

## Input and evidence gate

Require an approved script and a product image actually viewed. A product link substitutes only when its exact product images can be opened and visually inspected; page text alone is insufficient. If blocked, say: “Mình chưa xem được ảnh sản phẩm từ link này. Bạn gửi ảnh sản phẩm chính diện rõ nét để mình giữ đúng hình dáng nhé.” Stop product-locked final generation; preliminary shot planning may be clearly marked provisional. Resolve conflicts between link and photo with the user.

Preserve the approved story, hook, characters, artwork, actions and CTA. Add filming mechanics, not new plot. A pet/person in printed artwork is not a live scene character. Never infer invisible construction, health results, gift packaging or free personalization claims.

## Process

1. Establish verified product invariants, approved identities, setting and spatial layout. Read the script rather than borrowing details from examples. If adapting a source video, inspect it first and obtain approval for the adapted script before producing final assets.
2. Map the approved actions to chronological keyframes and feasible time intervals; panels do not imply equal-duration shots. If the duration cannot support the actions, ask before shortening the story or extending duration.
3. Produce the board using a real raster image-generation/editing tool with actual product and identity attachments. Inspect it, correct targeted errors, and keep the prompt aligned. A written filename is not an uploaded reference.
4. Write a FULL English prompt, one paragraph with no embedded newlines, following the templates. Bind tags to actual attachment names. Explicitly distinguish continuous motion from cuts, printed artwork from overlays, and board layout from full-screen video.
5. Apply the QA checklist and optional `scripts/check.py`. The script checks technical invariants only; visually verify panel count/product/story separately.
6. Deliver only files that exist, report text-only or unresolved items truthfully, and state what has not been tested. Do not install/publish/upload/render unless separately authorized.

## Tools and output boundaries

This skill contains no image or video model, credentials, scraping integration or upload integration. Use available authorized tools; never replace missing image generation with a fake PNG path, placeholder SVG, or claims of successful rendering. Without image generation, deliver `prompt.txt`, `img.txt` and the six-keyframe specification with explicit “storyboard PNG chưa được tạo”. Without verified product imagery, stop before final product-locked outputs instead.

Follow the user's output root/numeric project/section/version conventions where supplied. Otherwise agree a destination appropriate to the environment. Keep old revisions; no default ZIP. For a full kit explicitly requested, add original product reference and six separately generated scene assets plus the assembled board; don't present low-resolution crops as original high-resolution references. For only prompt + SB, two main assets suffice.

Never assume @tags, duration, audio, text rendering or reference modes work identically across applications. Ask the actual model/mode when troubleshooting; do not shorten prompts or bypass safety restrictions as a speculative fix.
