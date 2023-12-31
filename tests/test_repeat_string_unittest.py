
# Generated by CodiumAI

import unittest

class TestRepeatString(unittest.TestCase):

    #  Should return an empty string when times is less than 1
    def test_return_empty_string_when_times_less_than_1(self):
        # Arrange
        times = 0

        # Act
        result = repeat_string(times)

        # Assert
        self.assertEqual(result, "")

    #  Should return the string repeated 'times' number of times
    def test_return_string_repeated_times_number_of_times(self):
        # Arrange
        times = 3
        string = "abc"

        # Act
        result = repeat_string(times, string)

        # Assert
        self.assertEqual(result, "abcabcabc")

    #  Should return the default string '>' repeated 'times' number of times when no string is provided
    def test_return_default_string_repeated_times_number_of_times_when_no_string_provided(self):
        # Arrange
        times = 5

        # Act
        result = repeat_string(times)

        # Assert
        self.assertEqual(result, ">>>>>")

    #  Should return an empty string when times is equal to 0
    def test_return_empty_string_when_times_equal_to_0(self):
        # Arrange
        times = 0

        # Act
        result = repeat_string(times)

        # Assert
        self.assertEqual(result, "")

    #  Should return the string when times is equal to 1
    def test_return_string_when_times_equal_to_1(self):
        # Arrange
        times = 1
        string = "abc"

        # Act
        result = repeat_string(times, string)

        # Assert
        self.assertEqual(result, "abc")

    #  Should return an empty string when times is a negative integer
    def test_return_empty_string_when_times_negative_integer(self):
        # Arrange
        times = -2

        # Act
        result = repeat_string(times)

        # Assert
        self.assertEqual(result, "")
