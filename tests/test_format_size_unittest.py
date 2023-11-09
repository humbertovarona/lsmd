
import unittest

class TestFormatSize(unittest.TestCase):

    #  Returns '0.0 kB' when input is 0.
    def test_returns_zero_kB_when_input_is_zero(self):
        # Arrange
        input_size = 0
    
        # Act
        result = format_size(input_size)
    
        # Assert
        self.assertEqual(result, '0.0 kB')

    #  Returns '0.5 kB' when input is 512.
    def test_returns_zero_point_five_kB_when_input_is_512(self):
        # Arrange
        input_size = 512
    
        # Act
        result = format_size(input_size)
    
        # Assert
        self.assertEqual(result, '0.5 kB')

    #  Returns '1.0 kB' when input is 1024.
    def test_returns_one_kB_when_input_is_1024(self):
        # Arrange
        input_size = 1024
    
        # Act
        result = format_size(input_size)
    
        # Assert
        self.assertEqual(result, '1.0 kB')

    #  Returns '1023 B' when input is 1023.
    def test_returns_1023_B_when_input_is_1023(self):
        # Arrange
        input_size = 1023
    
        # Act
        result = format_size(input_size)
    
        # Assert
        self.assertEqual(result, '1023 B')

    #  Returns '1024.0 kB' when input is 1048576.
    def test_returns_1024_point_zero_kB_when_input_is_1048576(self):
        # Arrange
        input_size = 1048576
    
        # Act
        result = format_size(input_size)
    
        # Assert
        self.assertEqual(result, '1024.0 kB')

    #  Returns '1023.9 GB' when input is 1100000000000.
    def test_returns_1023_point_nine_GB_when_input_is_1100000000000(self):
        # Arrange
        input_size = 1100000000000
    
        # Act
        result = format_size(input_size)
    
        # Assert
        self.assertEqual(result, '1023.9 GB')
