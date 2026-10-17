# Hook formula and split mode (clips A and B)

## The sales-video formula

1. HOOK (0-3 s): something that stops the scroll and opens a question the viewer wants answered.
2. CURIOSITY / PIVOT (3-5 s): a short beat that points at the answer (a look, a pan, a "wait, what is that?").
3. PRODUCT REVEAL (unboxing): the product comes out of its box or packaging into the hero's hands.
4. USE / DEMONSTRATION: hold it beside the face, show the printed or visible details, hang or use it.
5. CHECK-IN / CTA: a final clean close-up of the product in place, with safe space for one call to action added in editing.

The hook is entertainment; the product part sells. Spend most of the video on lively, clear product presentation, not on a complicated hook story.

## Hook types that work as short physical or visual events

- Accident hook: a held object is dropped or spilled, then the camera pans to something that explains the day.
- Curiosity gap: a character reacts to something off-screen, camera follows the gaze to a display or a box.
- Interrupted routine: a character is about to do an ordinary thing and gets stopped by the surprise.
- POV: the camera is the hero's eyes opening the box.
Use one hook per video. The hook must be filmable in about 3-5 seconds.

## Physical-event rule (why hooks usually need SPLIT mode)

A storyboard panel freezes ONE state. If panel 1 shows the END state of an event (cup already on the floor), the video tool starts from that state and the event never happens. For any event with a before and after:

- Panel 1 shows the START state (object still in the hand, floor clean).
- A middle panel shows the event in progress (object leaving the hand, object just above the floor).
- A later panel shows the end state (object on the floor, spill visible).
- The prompt narrates the event as one continuous motion with a timeline: release, continuous fall with increasing speed, impact, settle, and an explicit hold of the end state for at least 0.7 s. Forbid hovering, slow motion, reverse motion, strings, a second copy of the object.
- The camera pan or cut away happens only AFTER the end state has been shown.

Put such a hook in its own clip (SPLIT mode) so its storyboard can start from the start state and so a failed hook can be regenerated without touching the product clip.

## Split mode: clip A (hook) and clip B (product)

- Clip A, about 8-10 s, hook location only. No product reveal unless the hook itself requires it. End on a clean frame, never mid-motion or mid-impact.
- Clip B, about 8-10 s, starts with a hard cut to the product scene (for example "now at home"). Never cut in the middle of a collision, impact or the moment a held object leaves a hand.
- Identity: attach clip A's storyboard (or the cast sheet) when generating clip B's storyboard, so faces, hair and wardrobe stay identical.
- Product: only clip B (or the part of A that needs it) carries the product reference; keep the printed artwork static and keep exactly one product unit in the whole story.
- Naming: `<code>_a` and `<code>_b`, tags `@<code>_a` and `@<code>_b`, plus `@product` in the clips that show the product.
- Merge: play A then B with a hard cut at A's end. No cross-dissolve needed; the hard cut matches the scene change. Edit once on the merged video (see edit-post.md).
- Reuse: one good clip A can be paired with several clips B (other products or colors), and several hooks can be tested against one clip B.
- Cost: two storyboards, two prompts, two generations, one merge. Do not split when the hook is simple and the scene never changes.

## Beat map for a 10-second clip with six panels

Panels are keyframes, not equal slots. A useful split for clip A (hook): 0-2 s start state, 2-3.5 s event begins, 3.5-4.5 s event in progress, 4.5-6 s impact and reaction, 6-8 s end state and reaction, 8-10 s camera pans to the curiosity target. For clip B (product): 0-1.5 s closed box, 1.5-3 s lid off, 3-4.5 s product lifted out, 4.5-6.5 s product beside the face, 6.5-8 s use (hang, hold, show), 8-10 s hero close-up with clean safe space.
