"""Regression checks use isolated temporary vaults, never the user's notes."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from vault import check, read_section, search


class VaultTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def note(self, name, body, status='researched'):
        (self.root / f'{name}.md').write_text(f'---\ntitle: {name}\ndate: 2026-11-02\ntags: [test]\nstatus: {status}\n---\n\n{body}', encoding='utf-8')

    def test_search_keeps_stub_status_and_ranks_title(self):
        self.note('Data Saving', 'Not researched yet.', 'stub')
        self.note('Other', 'Data saving examples.')
        hits = search(self.root, 'data saving')
        self.assertEqual(hits[0]['title'], 'Data Saving')
        self.assertEqual(hits[0]['status'], 'stub')
        self.assertEqual(search(self.root, '!!!'), [])

    def test_section_stops_at_peer_and_ignores_fenced_heading(self):
        self.note('Example', '# Example\n## First\nbody\n```text\n## Fake\n```\n### Child\nchild\n## Second\nother')
        result = read_section(self.root, 'Example', 'First')
        self.assertIn('child', result)
        self.assertNotIn('other', result)
        with self.assertRaises(ValueError):
            read_section(self.root, '../outside')

    def test_broken_links_embeds_and_code_examples(self):
        self.note('Example', '[[Missing]] ![[missing.png]]\n```text\n[[Placeholder]]\n```')
        errors = check(self.root)['errors']
        self.assertEqual(len(errors), 2)
        self.assertFalse(any('Placeholder' in error for error in errors))

    def test_hash_mismatch_and_path_escape_fail(self):
        data = b'example'
        (self.root / 'media.png').write_bytes(data)
        folder = self.root / '_Data'
        folder.mkdir()
        manifest = folder / 'visual-media-test.json'
        asset = {'path': 'media.png', 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
        manifest.write_text(json.dumps({'assets': [asset]}))
        self.assertEqual(check(self.root)['media_verified'], 1)
        (self.root / 'media.png').write_bytes(b'changed')
        self.assertTrue(check(self.root)['errors'])
        asset['path'] = '../outside'
        manifest.write_text(json.dumps({'assets': [asset]}))
        self.assertIn('escapes vault', check(self.root)['errors'][0])

    def test_metadata_failure(self):
        (self.root / 'Bad.md').write_text('No properties', encoding='utf-8')
        self.assertTrue(check(self.root)['errors'])

    def test_unrecorded_media_fails(self):
        folder = self.root / '_Media' / 'Roblox'
        folder.mkdir(parents=True)
        (folder / 'extra.png').write_bytes(b'extra')
        self.assertIn('no integrity record', check(self.root)['errors'][0])

    def test_inline_link_examples_are_ignored(self):
        self.note('Example', 'Use `[[Note Name]]` to add a link.')
        self.assertEqual(check(self.root)['errors'], [])


if __name__ == '__main__':
    unittest.main()
