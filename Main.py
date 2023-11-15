import Calculator.Log

lines = []
while True:
    line = input()
    if line == "LOG":
        print("\x1B[H\x1B[J")
        Calculator.Log.print_log()
    elif line == "q":
        print("\x1B[H\x1B[J")
    elif line == "=":
        # break
        print(lines)
    else :
        lines.append(line)

