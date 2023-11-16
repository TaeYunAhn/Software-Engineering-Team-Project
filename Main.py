import Calculator.operation.operation as calculate
from Calculator.ErrorProcess.isError import is_error as errorCheck

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
else:
    print("ERROR!")