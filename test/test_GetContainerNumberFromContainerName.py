import unittest
from utils.GetContainerNumberFromContainerName import get_container_number_from_container_name
from data.Containers import containers_with_number, containers_without_number


class GetContainerNumberFromContainerNameTest(unittest.TestCase):
    
    def test_get_container_number_from_container_name_matches(self):
        for d in containers_with_number:
            self.assertEqual(get_container_number_from_container_name(d), d['result'])
            
        
    def test_get_container_number_from_container_name_no_matches(self):
        for d in containers_without_number:
            self.assertEqual(get_container_number_from_container_name(d), d['result'])