import unittest
from utils.GuessEventType import guess_event_type
from data.Tags import tags

class GuessEventTypeTest(unittest.TestCase):
    
    def test_guess_event_type_matches(self):
        for t in tags:
            self.assertEqual(guess_event_type(t['name']), t['GuessEventTypeResult'])
            
    def test_guess_event_type_no_matches(self):
        self.assertEqual(guess_event_type('instagram - this is instagram'), '')