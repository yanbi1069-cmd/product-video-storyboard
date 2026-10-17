# Workflow rules

## Mode and characters

Pick SINGLE or SPLIT with the table in SKILL.md before any file is written, and tell the user the reason in one or two sentences. Show the character notice and confirm an approved user-made cast sheet (characters.md) first. The hook formula and split rules are in hooks.md.

## Script and product lock

Use the supplied script as authority. Clarify only consequential gaps. Missing hook/CTA/audio is not permission to invent them: omit if intentionally absent, otherwise ask or label a proposal for approval. Do not add injuries, pet actions, dialogue, flashbacks or a different setting. Preserve exact custom names/year/photo unless the user approves replacement artwork.

Inspect actual product silhouette, relative scale, visible finish/components, hole/cord, compartments and printed text. Don't claim a material or manufacturing method just from appearance. Request additional front/back/button photos if necessary to lock a fragile operation. Printing must stay static like ink, not animated faces or a screen. Never promise perfect text preservation under large flips; propose controlled motion or separately approved postproduction.

No unsupported benefits, free engraving, delivery promises, gift boxes, universal fit, or simulated medical before/after effectiveness. A daily-use demonstration is not proof of treatment outcomes.

## Keyframes and image creation

Default board: portrait 2:3, six equal cells, 2 columns x 3 rows; slots 1 top-left, 2 top-right, 3 middle-left, 4 middle-right, 5 bottom-left, 6 bottom-right. Thin dividers, full canvas, no large margins or technical labels. VIDEO is 9:16, not the board. Each panel shows one interpretable state, not a multi-action montage inside a cell.

Identity and product references stay the same across image calls. Keep clothing, hair, prop scale and room geometry stable. For live-action sales briefs, prefer slightly imperfect everyday phone imagery rather than glossy ad portraits. For animated/cartoon briefs, retain the requested art style instead of forcing photorealism.

If eight cells are approved, use two columns x four rows, update ALL panel names, timeline and image specification. Do not leave six-panel instructions in an eight-panel prompt. The board's ratio is then explicitly chosen with the user, not inherited automatically.

## Motion and emotional continuity

Specify who holds the product/cord, which hand supports it, when the loop rests securely, release order and final state. Reduce simultaneous intricate motions through clearer choreography without removing approved story beats. A hard cut can imply time passage, whereas a continuous take must not teleport people or objects.

For toppling props, lock base/pivot, force direction, continuous arc, landing side and final object orientation. Screen-left/right positions must not swap midway. A rear button may become occluded from a frontal camera; don't require it to remain visible and accidentally create a second front button. Rotation on hands differs from the person/camera turning.

Map emotion to action: relaxed brow/jaw/shoulders, appropriate gaze target, light concentration during manipulation, spontaneous small smile/reaction at payoff. Neither a constant forced smile nor an expressionless subdued performance is required. Do not equate happiness with efficacy evidence.

## Audio and language lock

Never rely on "no dialogue" to keep a clip silent. Always write the explicit lock from SKILL.md/templates.md (NO-SPEECH, or American-English-only exact dialogue) and name Chinese/Mandarin in it and in the Avoid list. Decide silence or exact lines from the approved script, never from habit. If the tool UI has a language/voice setting, set it to English (US) as well; the prompt lock is still required.

## Revisions after tests

Use actual resulting clip or exact error message, model, generation mode (ingredients/references/first frame) and UI duration. Distinguish rejected generation from incorrect visual output. Do not assume length caused rejection. Preserve approved concept and format; change the narrowest demonstrated failure. Mark v2/v3 rather than silently overwriting.

Fallback when a finished clip has wrong-language speech but the picture is good: keep the video, separate voice from music with a stem separator (Demucs `--two-stems=vocals`), keep the music stem, synthesize the corrected line (for example edge-tts `en-US-AndrewNeural` for an American male), time it to the original speech window, remix, then verify by transcription. Lip movement still follows the original language, so prefer regenerating when speech is prominent. Reference implementation: `scripts/edit/replace_voice.py` (verify with `scripts/edit/check_audio_language.py`), explained in edit-post.md.

If repeated generation cannot preserve a key invariant, report the specific failure and propose an approved change or editing workflow; don't claim the prompt guarantees fidelity. No external publication or fresh paid integrations without scope/authorization.
