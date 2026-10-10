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


class CheckerTests(unittest.TestCase):
    def test_package(self):
        self.assertEqual(checker.check_skill(MODULE.parents[1]), [])

    def test_outputs(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as temp:
            root = Path(temp)
            self.assertTrue(checker.check_output(root))
            (root / 'prompt.txt').write_text('Line one\nLine two', encoding='utf-8')
            (root / 'img.txt').write_text('Text-only image specification', encoding='utf-8')
            self.assertTrue(checker.check_output(root, True))
            (root / 'prompt.txt').write_text('Use [DURATION] seconds.', encoding='utf-8')
            self.assertTrue(checker.check_output(root, True))
            (root / 'prompt.txt').write_text('One complete paragraph.\n', encoding='utf-8')
            self.assertEqual(checker.check_output(root, True), [])
            (root / 'sb.png').write_bytes(b'not a png')
            self.assertTrue(checker.check_output(root))
            # Synthetic header tests header parsing, NOT actual renderable PNG validation.
            (root / 'sb.png').write_bytes(b'\x89PNG\r\n\x1a\n' + struct.pack('>I', 13) + b'IHDR' + struct.pack('>II', 600, 900))
            self.assertEqual(checker.check_output(root), [])
            (root / 'sb.png').write_bytes(b'\x89PNG\r\n\x1a\n' + struct.pack('>I', 13) + b'IHDR' + struct.pack('>II', 900, 600))
            self.assertTrue(checker.check_output(root))


if __name__ == '__main__':
    unittest.main()
