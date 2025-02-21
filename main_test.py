import unittest
import os 

from main import Input, Day1

class TestDay1(unittest.TestCase):

    def setUp(self):
        self.testCase1 = Input()
        self.testCase1.add_values(3, 4)
        self.testCase1.add_values(4, 3)
        self.testCase1.add_values(2, 5)
        self.testCase1.add_values(1, 3)
        self.testCase1.add_values(3, 9) 
        self.testCase1.add_values(3, 3)
        return super().setUp()
    
    def test_day1_part1(self):
        test_class = Day1()
        actual = test_class.part1(self.testCase1)
        expected = 11
        self.assertEqual(expected, actual)
    
    def test_day1_part2(self):
        test_class = Day1()
        actual = test_class.part2(self.testCase1)
        expected = 31
        self.assertEqual(expected, actual)

    def test_day1_parse_part1(self):
        test_class = Day1()
        input_file = os.path.join(os.getcwd(), "input.txt")
        test_case2 = test_class.parse_file(input_file)
        actual = test_class.part1(test_case2)
        expected = 1197984
        self.assertEqual(expected, actual)

    def test_day1_parse_part2(self):
        test_class = Day1()
        input_file = os.path.join(os.getcwd(), "input.txt")
        test_case2 = test_class.parse_file(input_file)
        actual = test_class.part2(test_case2)
        expected = 23387399
        self.assertEqual(expected, actual)