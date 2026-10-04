from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LinkTests(unittest.TestCase):
    def check(self, text):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'tools').mkdir()
            (root / 'docs').mkdir()
            shutil.copyfile(ROOT / 'tools/check_links.py', root / 'tools/check_links.py')
            (root / 'docs/index.md').write_text(text, encoding='utf-8')
            (root / 'docs/target.md').write_text('# Target', encoding='utf-8')
            (root / 'mkdocs.yml').write_text(json.dumps({'nav': [{'Home': 'index.md'}, {'More': [{'Target': 'target.md'}]}]}), encoding='utf-8')
            return subprocess.run([sys.executable, str(root / 'tools/check_links.py')], capture_output=True, text=True)

    def test_optional_link_title(self):
        result = self.check('[Target](target.md "Read more")')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_reference_link(self):
        result = self.check('[Target][destination]\n\n[destination]: missing.md')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('missing.md', result.stderr)

    def test_code_examples_are_not_navigation(self):
        result = self.check('~~~markdown\n[example](missing.md)\n~~~\n\n`[inline](missing.md)`')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_encoded_path_anchor_and_external_links(self):
        result = self.check('[Target](target%2Emd#section) [External](//example.com/path) [Section](#section)')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_image(self):
        result = self.check('![illustration](missing.png)')
        self.assertNotEqual(result.returncode, 0)

    def test_escaping_path(self):
        result = self.check('[escape](../mkdocs.yml)')
        self.assertNotEqual(result.returncode, 0)
