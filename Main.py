import Calculator.operation.operation as calculate
import math
from Calculator.ErrorProcess.isError import is_error as errorCheck
from Calculator.EasterEgg.easter_egg import easter_egg as easterEgg
from Calculator.ErrorProcess.isError import is_factorial_error as FactorialErrorCheck
lines = []
calculateFlag = False

while True:
    line = input()
    if line == "!":
        lines.append(line)
        calculateFlag = False
        break
    elif line == "=":
        calculateFlag = True
        break
    else:
        lines.append(line)

if(calculateFlag == False):
    if FactorialErrorCheck(lines):
        factorial_result = math.factorial(int(lines[0]))
        print('= ' + str(factorial_result))
    elif int(lines[0])< 0 :
        print("[SYSTEM] Out Of Range")
    else:
        print("[SYSTEM] INPUT ERROR!")

elif(calculateFlag == True):
    if errorCheck(lines):
        answer = calculate(lines)
        print(answer)
        if answer == 7532:
          easterEgg(7532)
        if answer == 1015:
            easterEgg(1015)
else:
    print("[SYSTEM] ERROR!")
