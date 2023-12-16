import Calculator.operation.operation as calculate
from Calculator.ErrorProcess.isError import is_error as errorCheck
from Calculator.EasterEgg.easter_egg import easter_egg as easterEgg

lines = []
while True:
    line = input()
    if line == "=":
        break
    else:
        lines.append(line)

if errorCheck(lines):
    answer = calculate(lines)
    print(answer)
    if answer == 7532:
        easterEgg(7532)
    if answer == 1015:
        easterEgg(1015)
        
else:
    print("[SYSTEM] ERROR!")
