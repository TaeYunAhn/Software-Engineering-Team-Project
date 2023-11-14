def operation(data):
    nums = []
    operator = []

    #에러 처리 코드 넣기(data에 값이 정상적으로 들어왔는지)
    #isError(data)

    for i in range(0 , len(data)):
        if i % 2 == 0:
            nums.append(int(data[i]))
        else:
            operator.append(data[i])


    #곱셈을 먼저 모두 처리하고 덧셈만 남김

    answer = nums[0]
    i = 0
    while i < len(operator):
        if i >= len(operator):
            break
        if operator[i] == "*":
            nums[i] = nums[i]*nums[i+1]
            del nums[i+1]
            del operator[i]
            i -= 1
        i += 1

    #나머지 덧셈뺄셈 처리
    for i in range(0,len(operator)):
        if operator[i] == "+":
            answer += nums[i+1]
        elif operator[i] == "-":
            answer -= nums[i+1]
    return answer