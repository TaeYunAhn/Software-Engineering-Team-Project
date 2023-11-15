def operation(data):
    nums = []
    operator = []
    log = []

    # 에러 처리 코드 넣기(data에 값이 정상적으로 들어왔는지)
    # isError(data)

    for i in range(0, len(data)):
        if i % 2 == 0:
            nums.append(int(data[i]))
        else:
            operator.append(data[i])

    # 곱셈을 먼저 처리하고 덧셈만 남김
    i = 0
    while i < len(operator):
        if i >= len(operator):
            break
        if operator[i] == "*":
            nums[i] = nums[i] * nums[i + 1]
            del nums[i + 1]
            del operator[i]
            i -= 1
        else:
            i += 1

    # 나머지 덧셈 뺄셈 처리
    answer = nums[0]
    for i in range(0, len(operator)):
        if operator[i] == "+":
            answer += nums[i + 1]
        elif operator[i] == "-":
            answer -= nums[i + 1]

    # 입력 받은 연산식과 계산 결과를 로그에 저장
    equation = " ".join(data)
    log.append(equation + " = " + str(answer))

    return answer, log
