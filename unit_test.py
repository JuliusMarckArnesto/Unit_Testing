import unittest
from methods import methodss

class TestFizzBuzz(unittest.TestCase):
    
    def test_multiple_of_3_and_5(self):
        self.assertEqual(methodss(15), "fizzBuzz")
        self.assertEqual(methodss(30), "fizzBuzz")
    
    def test_multiple_of_3(self):
        self.assertEqual(methodss(6), "fizz")
        self.assertEqual(methodss(12), "fizz")
    
    def test_multiple_of_5(self):
        self.assertEqual(methodss(5), "buzz")
        self.assertEqual(methodss(10), "buzz")
    
    def test_invalid(self):
        self.assertEqual(methodss(7), "Invalid 7")
        
    
    def test_negative_numbers(self):
        self.assertEqual(methodss(-15), "fizzBuzz")
        self.assertEqual(methodss(-9), "fizz")
        self.assertEqual(methodss(-10), "buzz")
        self.assertEqual(methodss(-7), "Invalid -7")

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            methodss(4.5)
        with self.assertRaises(TypeError):
            methodss("hello")
        with self.assertRaises(TypeError):
            methodss(None)


if __name__ == "__main__":
    unittest.main()
