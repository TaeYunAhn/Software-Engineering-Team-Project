import Calculator.operation.operation as caluate

lines = []
while True:
    line = input()
    if line == "=":
        break
    else :
        lines.append(line)
        

caluate(lines)
