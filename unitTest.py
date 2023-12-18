import unittest
import math
from Calculator.EasterEgg.easter_egg import *
from Calculator.ErrorProcess.isError import *

class TestFactorial(unittest.TestCase):
    def test_factorial(self): 
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(-1), "[Error] Out Of Range")
        self.assertEqual(factorial(0), 1)

class TestEasterEgg(unittest.TestCase):
    def test_easter_egg(self):
        self.assertTrue(easter_egg(7503), "[EVENT] 안녕! 7503는 사용할 수 없는 숫자야")
        self.assertTrue(easter_egg(1015), "[EVENT] 전북대 개교기념일입니다.")
        self.assertIsNone(easter_egg(1234))

class TestIsError(unittest.TestCase):
    def test_is_error(self):
        self.assertFalse(is_error("5*-6-7")) # 숫자나 연산자가 연속으로 들어온 경우
        self.assertFalse(is_error("3/5")) # 더하기, 빼기, 곱하기 이외의 연산자가 들어온 경우
        self.assertFalse(is_factorial_error(["-5", "!"]))  # 0 이상의 정수인지 확인 
        self.assertFalse(is_factorial_error(["5", "+"]))   # 두 번째 기호가 !인지 확인
        self.assertFalse(is_factorial_error(["3","5", "!"])) # 두 개 이상의 숫자가 입력된 경우


def factorial(test_num):
    if test_num < 0:
        return "[Error] Out Of Range"
    else:
        return math.factorial(test_num)

# 예시 코드
if __name__ == '__main__':
    unittest.main()
