"""Local structural-helper unit tests; does not test agent/model performance."""
import importlib.util
from pathlib import Path
import struct
import tempfile
import unittest

MODULE = Path(__file__).parent / 'product-video-storyboard/scripts/check.py'
spec = importlib.util.spec_from_file_location('checker', MODULE)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

LOCK = ('Audio: quiet room tone. Nobody speaks: mouths stay closed or move only in natural non-verbal reactions; '
        'no lip-synced speech, narration or singing in any language, in particular no Chinese or Mandarin voices. '
        'Avoid Chinese or Mandarin speech.')
PROMPT = 'Use @demo as a six-panel storyboard. One complete paragraph. ' + LOCK
PROMPT_A = 'Use @demo_a as a six-panel storyboard for the hook clip. ' + LOCK
PROMPT_B = 'Use @demo_b as a six-panel storyboard. The clip begins with a HARD CUT from the hook clip. ' + LOCK


def fake_png(path, w=600, h=900):
    # Synthetic header tests header parsing, NOT actual renderable PNG validation.
    path.write_bytes(b'\x89PNG\r\n\x1a\n' + struct.pack('>I', 13) + b'IHDR' + struct.pack('>II', w, h))


class CheckerTests(unittest.TestCase):
    def test_package(self):
        self.assertEqual(checker.check_skill(MODULE.parents[1]), [])

    def test_single_outputs(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as temp:
            root = Path(temp)
            self.assertTrue(checker.check_output(root))
            (root / 'prompt.txt').write_text('Line one\nLine two', encoding='utf-8')
            (root / 'img.txt').write_text('Text-only image specification', encoding='utf-8')
            self.assertTrue(checker.check_output(root, True))
            (root / 'prompt.txt').write_text('Use [DURATION] seconds.', encoding='utf-8')
            self.assertTrue(checker.check_output(root, True))
            (root / 'prompt.txt').write_text(PROMPT + '\n', encoding='utf-8')
            self.assertEqual(checker.check_output(root, True), [])
            (root / 'sb.png').write_bytes(b'not a png')
            self.assertTrue(checker.check_output(root))
            fake_png(root / 'sb.png')
            self.assertEqual(checker.check_output(root), [])
            fake_png(root / 'sb.png', 900, 600)
            self.assertTrue(checker.check_output(root))

    def test_audio_lock_required(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as temp:
            root = Path(temp)
            fake_png(root / 'sb.png')
            # "no dialogue" alone must fail: this exact wording once produced Mandarin speech.
            (root / 'prompt.txt').write_text('Use @demo as storyboard. Audio: room tone, no spoken dialogue.', encoding='utf-8')
            errors = checker.check_output(root)
            self.assertTrue(any('Chinese' in e for e in errors), errors)
            (root / 'prompt.txt').write_text('Use @demo as storyboard. Cut quickly.', encoding='utf-8')
            self.assertTrue(any('Audio' in e for e in checker.check_output(root)))
            (root / 'prompt.txt').write_text(
                'Use @demo as storyboard. Dialogue (American English only, never Chinese or any other language): she says exactly "Hi" at 2-3s.',
                encoding='utf-8')
            self.assertEqual(checker.check_output(root), [])

    def test_split_outputs(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as temp:
            root = Path(temp)
            for name, text in (('a', PROMPT_A), ('b', PROMPT_B)):
                (root / name).mkdir()
                (root / name / 'prompt.txt').write_text(text, encoding='utf-8')
                fake_png(root / name / 'sb.png')
            self.assertEqual(checker.check_output(root), [])
            (root / 'b' / 'prompt.txt').write_text(PROMPT_B.replace('HARD CUT', 'cut'), encoding='utf-8')
            self.assertTrue(any('hard cut' in e for e in checker.check_output(root)))
            (root / 'b' / 'prompt.txt').write_text(PROMPT_B.replace('@demo_b', '@demo'), encoding='utf-8')
            self.assertTrue(any('_b' in e for e in checker.check_output(root)))
            (root / 'b' / 'prompt.txt').write_text(PROMPT_B, encoding='utf-8')
            (root / 'a' / 'sb.png').unlink()
            self.assertTrue(any(e.startswith('clip a') for e in checker.check_output(root)))


if __name__ == '__main__':
    unittest.main()
