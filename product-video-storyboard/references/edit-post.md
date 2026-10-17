# Post-production edit for short product sales videos

Applies to finished clips (single clips, or clip A + clip B merged). Typical example: a personalized holiday ornament video, but the rules fit any product. Everything here is optional guidance plus three helper scripts in `scripts/edit/`. Never post or upload anything unless the user explicitly asks.

## Principles

1. Look at the REAL render first (contact sheet or frames at 0 s, 2 s, 4 s, middle, end). Prompt timelines do not match the actual video.
2. Do not change the story: no cuts, reordering or speed changes unless the user asks. The footage is usually complete; only trim dead time if requested.
3. Save the edit as a new versioned file (`<code>_edit_v1.mp4`). Keep the source untouched.
4. Be honest about what was checked. Frames and a transcript are not the same as listening to the whole video.
5. Rendering to 1080x1920 from a 720x1280 source is an upscale; do not claim added detail.

## Text rules (hook, middle text, call to action)

- HOOK at the start (about 3.5 s): one or two short lines in English that fit what the viewer sees. No background box; use warm white text with a dark outline and a soft shadow. Optional small seasonal icons above it (the bundled Twemoji tree and gift are Christmas icons; leave them out for other occasions, and credit Twemoji CC-BY 4.0 if you publish with them).
- MIDDLE TEXT while the product is shown: one message about personalization that is TRUE for the product. Check the product page: if only names and the year can be customized, say "Personalize it with your own names." If photos are supported too, say "names and photos". Never promise features the page does not state.
- CALL TO ACTION near the end: only if the clip does not already end with one. One action only, for example "Make it yours. Shop the link in bio." Do not stack several asks (tag, save, comment keyword and click) in one video.
- Placement: never cover faces, the product, printed lettering, hands doing the key action, or the bottom and side interface margins of the platform. Choose the top area when the lower area is busy and the other way round. If a line collides with something, move it or shorten it; verify on real frames.
- Moving a text block is cheap: re-render and look again.

## Audio rules

Pick ONE policy per video:

- KEEP the original audio (default when it contains approved music or the dialogue you want). Do not cut the footage in a way that breaks the music; do not add a second music bed on top.
- REPLACE the music: mute ALL original audio first, then use one continuous royalty-free track with a short fade in and out. Layering new music over music already in the clip sounds chaotic.
- COUNTING or voice-over only when the story has a count-then-reveal moment, timed to the visible action. Do not add voice-over by habit.

## Check the spoken language (mandatory)

Video tools sometimes invent speech in a default language even when the prompt says "no dialogue". After generating, run:

`python scripts/edit/check_audio_language.py clip.mp4 --expect none` (clips that must be silent of speech)
`python scripts/edit/check_audio_language.py clip.mp4 --expect en` (clips with approved English lines)

Requires `pip install faster-whisper` and ffmpeg. The result is a heuristic; confirm borderline cases by listening.

## Voice replacement fallback (when the picture is good but the voice is wrong)

`python scripts/edit/replace_voice.py --video clip.mp4 --parts parts.json --out-audio fixed.wav --mux fixed.mp4`

It separates the voice from the music with Demucs, keeps the music, synthesizes your corrected lines with edge-tts (for example `en-US-AndrewNeural` for an American male voice, `en-US-AriaNeural` for a female voice), places them in the original speech window and remixes. Notes:
- The speech window and the corrected lines go into `parts.json` (see the script docstring). Split a long line at natural pauses to match the original rhythm.
- The synthetic voice is not a real actor and the lip movement still follows the original language. When speech is prominent on screen, regenerating the clip with a stronger audio lock is usually better.
- Installation: a virtual environment with a SHORT path on Windows (torch has very long internal paths), then `pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu`, `pip install demucs edge-tts`.
- edge-tts sends the text of the lines to an online speech service. Do not use it for private text.
- Always verify with `check_audio_language.py --expect en` afterwards.

## Build and render the text overlay edit

1. Write a `spec.json` as shown in the docstring of `scripts/edit/build_edit.py` (hook, middle text, call to action with start times and `top` positions in a 1080x1920 canvas, and the audio mode).
2. `python scripts/edit/build_edit.py spec.json` creates a HyperFrames project folder.
3. In that folder: `npx --yes hyperframes@0.8.160 check`, then `npx --yes hyperframes@0.8.160 render --quality delivery --output renders/clip_edit_v1.mp4`. HyperFrames is an external open-source video tool; it needs Node.js. Pin the version you tested.
4. Extract frames from the render, confirm the text, then run the audio language check again on the final file.
5. Hand the file to the user for approval. Posting is a separate decision.

## Reporting

Say what was done (texts added, audio policy, versions), what was verified (frames viewed, transcript language) and what was not (full listening, lip-sync, motion realism).
