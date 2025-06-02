import unittest
from utils.DupeKey import guess_var_from_tool, dupe_key
from data.Data import data

class DupeKeyTest(unittest.TestCase):

    def test_guess_var_from_tool_known(self):
        self.assertEqual(guess_var_from_tool('cm'), 'session_id:')
        self.assertEqual(guess_var_from_tool('aw'), 'transaction_id:')
        self.assertEqual(guess_var_from_tool('facebook'), 'eventID:')

    def test_guess_var_from_tool_unknown(self):
        self.assertEqual(guess_var_from_tool('instagram'), '')

    def test_dupe_key_with_matches(self):
        for d in data:
          result = dupe_key(d['tool'], d['script'])
          self.assertEqual(d['dupeKeyResult'], result)

    def test_dupe_key_no_matches(self):
        tool = 'aw'
        script = 'var transaction_idx:99999;'
        result = dupe_key(tool, script)
        self.assertEqual(result, '')

    def test_dupe_key_no_var(self):
        tool = 'unknown'
        script = 'any script content'
        result = dupe_key(tool, script)
        self.assertEqual(result, '')
