import Calculator.operation.operation as calculate
import Calculator.ErrorProcess.isError as isError

lines = []
while True:
    line = input()
    if line == "=":
        break
    else:
        lines.append(line)

if isError.is_error(lines):
    answer = calculate(lines)
    print(answer)
else:
    print("ERROR!")