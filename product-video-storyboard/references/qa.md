# Delivery QA

- Actually viewed the correct product image; conflicts resolved, custom artwork approved.
- Every main script action accounted for, no added pet/person/benefit/packaging/dialogue.
- Exactly six equal cells 2x3 and correct reading order, or explicitly agreed eight-cell variant with all instructions updated.
- Keyframes interpretable, identities/clothes/prop scale/layout stable, hands and text inspected.
- Product silhouette/components/printed artwork match, printed subjects aren't additional live characters.
- Timings cover requested duration without accidental gaps/overlap, cuts distinguish time jumps.
- Force direction/rotation/occlusion/release make sense; end states match next keyframes.
- Emotion matches voluntary actions, not frozen smile or forced blank expression.
- English FULL single paragraph, no embedded newline or unresolved template slots.
- Actual attachment names/tags documented; no assertion that tags work universally.
- Text/audio exactly follow approved brief; CTA timing and safe placement where present.
- Mode choice (SINGLE or SPLIT) was explained with the table in SKILL.md; in SPLIT mode the cut sits between hook and product, never inside an impact.
- The character notice was shown and an approved user-made cast sheet is attached; no characters came from memory, earlier projects or another channel.
- SPLIT mode: each clip has its own 2x3 board and prompt; clip A panel 1 shows the START state (not the end state); the end state is held at least 0.7 s before any pan; clip B starts with a hard cut, attaches clip A's board as identity reference, has exactly one product unit; tags end in `_a` and `_b`; `note.md` gives the merge order.
- Audio and language lock present: an explicit NO-SPEECH lock or an American-English-only exact-dialogue lock, and the Avoid list names Chinese/Mandarin and other non-English speech. "No dialogue" alone fails this check. `scripts/check.py output` enforces it.
- Real sb.png visually inspected, or explicit text-only status + img.txt. Technical checks alone don't prove six panels.
- Correct requested folder/version, no overwrites of approved version or unsolicited ZIP.
- No claim of video test/render/cloud upload when none occurred.

## Audio language check on the real video (mandatory before editing or posting)

Run `python scripts/edit/check_audio_language.py clip.mp4 --expect none` (or `--expect en`). It extracts the audio and transcribes it with automatic language detection (faster-whisper, local). Manual equivalent:
`ffmpeg -y -i clip.mp4 -vn -ac 1 -ar 16000 a.wav` then `WhisperModel('small').transcribe('a.wav')` and read `info.language` plus the segments.
- NO-SPEECH clip: no speech segments (music/ambience only) is the pass. Any recognized speech is a failure.
- Dialogue clip: language must be `en` and the text must match the approved line.
- Report the detected language and text to the user. If a wrong-language voice exists, do not silently post: regenerate with a stronger lock or replace the voice (workflow.md fallback).

Manual behavioral cases for future testing (not claimed as model-tested):

1. Unreadable product URL + clear story: request image, do not invent shape.
2. Photo of owner/pet printed on ornament, no live pet in story: don't add a live dog.
3. Approved no-text/no-speech: don't add CTA or voiceover from examples.
4. Custom name/year differs from example: preserve supplied artwork, not example names.
5. Too many actions for 10s: ask before removing a beat.
6. Rear-only button, frontal person: show/rotate the prop as approved, allow button occlusion; no duplicate button.
7. No image tool: explicit text-only kit, no synthetic file claim.
8. Approved cartoon style: retain cartoon look, not generic photorealism.
9. Revision requested: same project new version, not new project number.
10. Script says "no dialogue": prompt must still carry the NO-SPEECH lock naming Chinese/Mandarin, not only "no dialogue".
11. Script has a spoken line: prompt must carry the American-English-only dialogue lock with the exact line and time window.
12. Hook where an object is dropped, then the scene moves to another place: choose SPLIT, clip A panel 1 shows the object still in the hand, not on the floor.
13. User has no cast sheet: help create one; do not reuse characters from memory, notes or another channel.
14. Simple single-room demo with no object event: choose SINGLE and say why.
