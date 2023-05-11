import unittest

import sys
sys.path.append('..')

from src.read_log_file_graalvm import get_parsed_data_from_file

def contains(string_list, text):
    for s in string_list:
        if text in s:
            return True
    return False

class Test_parsing_groups(unittest.TestCase):

    def setUp(self):
        log_file = "../datasets/parse_log_file_graalvm_test.log"
        # log_file = "../datasets/parse_log_file_test.log"
        self.gc_event_dataframes = get_parsed_data_from_file(log_file)
        # self.additional_event_infos = gc_event_dataframes["AdditionalEventInfo"]

    def test_time(self):
        self.assertEqual(37400, self.gc_event_dataframes["Time"][0])

    def test_event_type(self):
        self.assertEqual("Full GC", self.gc_event_dataframes["EventType"][0])

    def test_heap_before_gc(self):
        self.assertEqual(26624, self.gc_event_dataframes["HeapBeforeGC"][0])

    def test_heap_after_gc(self):
        self.assertEqual(5120, self.gc_event_dataframes["HeapAfterGC"][0])

    def test_duration_ms(self):
        self.assertEqual(6.717, self.gc_event_dataframes["Duration_milliseconds"][0])

if __name__ == "__main__":
    unittest.main()
