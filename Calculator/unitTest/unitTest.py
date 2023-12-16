import unittest
import math
from Calculator.EasterEgg.easter_egg import *
from Calculator.ErrorProcess.isError import *

class test_factorial(unittest.TestCase):
    def FactorialTest(self): 
        self.assertEqual(factorial("3"),"6")
        self.assertEqual(factorial("-1"),"[Error] Out Of Range")
        self.assertEqual(factorial("0"),"1")

class test_easteregg(unittest.TestCase):
    def EasterEggTest(self):
        self.assertEqual(easter_egg(answer="1015"), second= "[EVENT] 전북대 개교기념일입니다.")
        self.assertEqual(easter_egg(answer="7532"), second= "[EVENT] 안녕! 7532는 사용할 수 없는 숫자야")

class test_isError(unittest.TestCase):
    def isErrorTest(self):
        self.assertFalse(is_error("3+")) # 숫자나 연산자가 연속으로 들어온 경우
        self.assertFalse(is_error("/")) # 더하기, 빼기, 곱하기 이외의 연산자가 들어온 경우
        self.assertFalse(is_factorial_error("-3")) # 첫 번째 요소가 0 이상의 정수인지 확인
        self.assertTrue(is_factorial_error("!")) # 두 번째 요소가 '!' 기호인지 확인


def factorial(test_num):
    if(len(test_num)<= 0):
        return test_num
    else :
        return math.factorial(test_num)

#예시코드
if __name__ == '__main__':
    unittest.main()
