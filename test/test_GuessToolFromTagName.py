import unittest
from utils.GuessToolFromTagName import guess_tool_from_tag_name
from data.Tags import tags

class GuessToolFromTagNameTest (unittest.TestCase):
    
    def test_guess_tool_from_tag_name_matches (self):
        for t in tags:
            self.assertEqual(guess_tool_from_tag_name(t['name']), t['GuessToolFromTagNameResult'])
            
    def test_guess_tool_from_tag_name_no_matches (self):
        self.assertEqual(guess_tool_from_tag_name('instagram - prochainement'), '')