import unittest
import math

class testFactorial(unittest.TestCase):
    def factorial(self): 
        self.assertEqual(factorial("3"),"6")
        self.assertEqual(factorial("7"),"5040")
        self.assertEqual(factorial("12"),"479001600")
        self.assertEqual(factorial("1"),"1")
        self.assertEqual(factorial("0"),"1")

def factorial(test_num):
    if(len(test_num)<= 0):
        return test_num
    else :
        return math.factorial(test_num)

def  capitalize_first_letter(test_string):
    if(len(test_string)<= 0):
        return test_string
    if(test_string[0].islower()):
        test_string = test_string[0].upper() + test_string[1:]
    return test_string

#예시코드
if __name__ == '__main__':
    unittest.main()
