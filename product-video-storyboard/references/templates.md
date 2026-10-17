# Templates — fill, adapt and remove placeholders

These are structural examples, not ready-to-run prompts. Read the script and verified product evidence first. The quoted examples do not add mandatory characters, ornament shapes, pets, dialogue, Christmas music or CTA to new briefs.

## Single clip: video prompt sequence (1 storyboard + 1 prompt)

1. Storyboard binding, layout/order, duration, video 9:16, panels as keyframes, full-screen/no grid.
2. Product invariants and static print where relevant.
3. Character identity and approved setting/layout.
4. Approved concept only.
5. Each time interval: panel slot, cut/continuation, framing, camera, action/direction, hand roles and end state.
6. Exact approved overlay/CTA with timings, typography and safe area, or explicit no-text requirement when requested.
7. Requested visual style, then the MANDATORY audio and language lock: either the NO-SPEECH lock or the American-English-only exact-dialogue lock (see SKILL.md). Never write only "no dialogue".
8. Relevant product/identity/physics errors to avoid, not contradictory prohibitions.

English single-paragraph scaffold:

Use @storyboard as a six-panel portrait storyboard arranged in two columns and three rows for one [DURATION]-second vertical 9:16 [APPROVED STYLE] video, reading left to right across each row, then top to bottom: panel 1 top-left, panel 2 top-right, panel 3 middle-left, panel 4 middle-right, panel 5 bottom-left, panel 6 bottom-right. Use these as chronological keyframes, not simultaneous images or equal-duration clips; every shot fills the entire frame without borders, labels, a collage or split screens. Use @product as the exact reference for [VERIFIED PRODUCT INVARIANTS]; [STATIC PRINT RULE IF APPLICABLE]. Keep the same [APPROVED IDENTITIES] in [APPROVED SETTING AND SPATIAL LAYOUT]. Follow only [APPROVED STORY]. From [0] to [T1]s, following panel 1 top-left, [FRAMING, ACTION, DIRECTION AND END STATE]. From [T1] to [T2]s, following panel 2 top-right, [CUT OR CONTINUATION, CAMERA, ACTION AND END STATE]. From [T2] to [T3]s, following panel 3 middle-left, [SHOT DETAILS]. From [T3] to [T4]s, following panel 4 middle-right, [SHOT DETAILS AND HAND ROLES]. From [T4] to [T5]s, following panel 5 bottom-left, [SHOT DETAILS AND RELEASE/CONTINUITY]. From [T5] to [DURATION]s, following panel 6 bottom-right, [FINAL SHOT AND END STATE]. [EXACT APPROVED OVERLAYS WITH TIMING AND SAFE AREA, OR NO-TEXT RULE IF REQUESTED]. [APPROVED LOOK AND EMOTION ARC]. [AUDIO AND LANGUAGE LOCK: use ONE of the two blocks below]. Avoid [SPECIFIC RELEVANT ERRORS], including Chinese or Mandarin speech, any non-English speech, unrequested speech or narration, model-generated subtitles.

Audio and language lock blocks (copy one, fill the brackets, never omit):

- NO-SPEECH (default): Audio: [AMBIENCE AND SFX]. Nobody speaks: mouths stay closed or move only in natural non-verbal reactions (smile, gasp, laugh, breath); no lip-synced speech, narration or singing in any language, in particular no Chinese or Mandarin voices; no added music unless approved.
- EXACT DIALOGUE (only when the approved script contains the line): Dialogue (American English only, never Chinese or any other language): [SPEAKER] says exactly "[LINE]" at [T1]-[T2]s in a natural American [MALE/FEMALE] voice with synchronized lips; no other speech.

Replace tag names to match the app's attachments, never assume @tags upload anything. Output one line without brackets left over, Markdown fences or user-facing instructions. FULL means complete actionable detail, not a fixed word count. Omit irrelevant scaffold clauses, not necessary mechanics. Duration/audio support must be checked against the actual generation UI when needed.

## Split clips A and B (2 storyboards + 2 prompts)

Use when SKILL.md says SPLIT (location or time change, or a hook with a physical event). Read hooks.md first. The characters come only from the user's approved cast sheet: write identities as `[HERO]: [HAIR, FACE, WARDROBE FROM THE APPROVED SHEET]`, never from this repository.

Clip A (hook) scaffold, one paragraph:

Use @[CODE]_a as a six-panel portrait storyboard arranged in two columns and three rows for ONE [8-10]-second vertical 9:16 [APPROVED STYLE] hook clip, reading left to right across each row, then top to bottom. The six panels are chronological keyframes, not simultaneous images or six clips; every shot fills the entire frame without borders, labels, a collage or split screens. Use @[CODE]_a as identity authority for [HERO] and [PARTNER]: [APPROVED IDENTITY TEXT]. Opening lock: [HOOK LOCATION, SPATIAL LAYOUT, CAMERA SIDE]; [HERO] holds [ONE HOOK OBJECT] in [HAND] at [HEIGHT]; the floor or surface is clean and the object is NOT yet fallen. Treat panel 1 as the START state. From 0 to [T1]s, following panel 1, [START STATE AND NORMAL ACTION]. From [T1] to [T2]s, following panel 2, [EVENT BEGINS: THE OBJECT LEAVES THE HAND, FINGERS OPEN, CONTACT BROKEN]. From [T2] to [T3]s, following panel 3, [EVENT IN PROGRESS: CONTINUOUS MOTION WITH INCREASING SPEED, NO HOVERING OR SLOW MOTION]. From [T3] to [T4]s, following panel 4, [IMPACT, SETTLE, REACTIONS]. From [T4] to [T5]s, following panel 5, [HOLD THE END STATE VISIBLY FOR AT LEAST 0.7 SECONDS]. From [T5] to [DURATION]s, following panel 6, [CAMERA PAN OR REFRAME TO THE CURIOSITY TARGET ONLY AFTER THE END STATE; OBJECT LEAVES THE FRAME]. End on a clean frame, not mid-motion. One hook object in total. Clean footage with no burned-in lettering or CTA. [APPROVED LOOK, EXPRESSIONS AND REAL-PHONE IMPERFECTIONS]. [AUDIO AND LANGUAGE LOCK]. Avoid [HOOK PHYSICS ERRORS], a second copy of the object, [IDENTITY AND SET ERRORS], Chinese or Mandarin speech, any non-English speech, unrequested speech or narration, model-generated subtitles.

Clip B (product) scaffold, one paragraph:

Use @[CODE]_b as a six-panel portrait storyboard arranged in two columns and three rows for ONE [8-10]-second vertical 9:16 [APPROVED STYLE] product clip that begins with a HARD CUT from the hook clip, reading left to right across each row, then top to bottom. [SAME FRAME RULES AS CLIP A]. Use @product as the exact reference for [VERIFIED PRODUCT INVARIANTS]; [STATIC PRINT RULE]; only ONE product unit exists in the whole video. The cast is the SAME [HERO] and [PARTNER] as in @[CODE]_a with identical faces, hair and wardrobe: [APPROVED IDENTITY TEXT]. Scene lock: [PRODUCT SCENE, FURNITURE LAYOUT, CAMERA SIDE, LIGHT]. Packaging lock: [PACKAGING DESCRIPTION; a staging prop, not a claim about official packaging]. From 0 to [T1]s, following panel 1, [PACKAGE CLOSED, CHARACTERS LEAN IN]. From [T1] to [T2]s, following panel 2, [LID OFF, WITHOUT STRETCHING OR UNTYING ANYTHING]. From [T2] to [T3]s, following panel 3, [PRODUCT LIFTED OUT BY A DEFINED HOLD POINT]. From [T3] to [T4]s, following panel 4, [PRODUCT BESIDE THE FACE, PRINTED SIDE TOWARD CAMERA, FINGERS NOT COVERING PRINT]. From [T4] to [T5]s, following panel 5, [USE OR PLACEMENT, HAND ROLES AND RELEASE ORDER]. From [T5] to [DURATION]s, following panel 6, [FINAL HERO CLOSE-UP, PRODUCT IN THE UPPER TWO-THIRDS, CLEAN SAFE SPACE, NO PEOPLE OR HANDS]. Clean footage; add any CTA in editing only. [APPROVED LOOK]. [AUDIO AND LANGUAGE LOCK]. Avoid [PRODUCT AND IDENTITY ERRORS], a duplicated or altered product, covered print, Chinese or Mandarin speech, any non-English speech, unrequested speech or narration, model-generated subtitles.

Merge A then B with a hard cut at the end of A. Save as `<code>/a/prompt.txt`, `<code>/a/sb.png`, `<code>/b/prompt.txt`, `<code>/b/sb.png` and a short `note.md`.

## Storyboard image instruction (single clip or each clip of a split)

Create one portrait [APPROVED STYLE] storyboard with exactly SIX EQUAL panels arranged in TWO COLUMNS and THREE ROWS, left to right then top to bottom, filling the canvas with thin dividers and no outer margins, technical labels or scene numbering. Use the attached verified product image as the product authority, and attached identity images when supplied. Keep [CHARACTERS/CLOTHING] and [ROOM GEOMETRY] consistent. Top-left: [KEYFRAME 1]. Top-right: [KEYFRAME 2]. Middle-left: [KEYFRAME 3]. Middle-right: [KEYFRAME 4]. Bottom-left: [KEYFRAME 5]. Bottom-right: [KEYFRAME 6]. Preserve [VERIFIED SHAPE, SCALE, COMPONENTS AND ARTWORK]. [STATIC PRINT RULE WHEN APPLICABLE]. [APPROVED LOOK]. [ONLY APPROVED TEXT IN SPECIFIED PANELS, SAFE PLACEMENT]. No additional characters, claims, logos, watermarks or unapproved story changes.

For SPLIT mode: clip A's board shows the START state in panel 1 (object in the hand, clean floor) and the end state only in later panels. Clip B's board is generated with clip A's board (or the cast sheet) attached as the identity reference plus the product image; its last panel shows the product alone. Never attach another creator's characters.

Attach actual images. An example board is a layout reference only, not a source of cast/product/story. Inspect the generated pixels before final delivery. If exact overlays are not generated cleanly, correct them with available authorized editing tools or disclose the issue; do not silently change their wording.
