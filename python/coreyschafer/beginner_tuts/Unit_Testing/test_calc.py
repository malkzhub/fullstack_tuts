import unittest
import calc


class TestCalc(unittest.TestCase):

    ## When testing it is recommended to use (test_) at the start of the method
    def test_add(self):
        # result = calc.add(10, 5)
        # self.assertEqual(result, 15) # Correct
        # self.assertEqual(result, 14) # AssertionError

        ## Edge Case
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


    def test_subtract(self):

        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):

        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        ## Testing Dividing by zero raises the correct error (Start again at 16:00 Corey Schafer YT)

        # ## First Way
        # self.assertRaises(ValueError, calc.divide, 10, 0)

        ## Second Way - Using Context Manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


## script in order not to run python -m unittest file.py in terminal
if __name__ == '__main__':
    unittest.main()

## Unit testing will run normally in the terminal