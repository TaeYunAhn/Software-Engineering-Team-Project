def operation(data):
    nums = []
    operator = []

    #에러 처리 코드 넣기(data에 값이 정상적으로 들어왔는지, 연산자가 여러개 들어오진 않았는지)
    #isError(data)

    for i in range(0 , len(data)):
        if i % 2 == 0:
            nums.append(int(data[i]))
        else:
            operator.append(data[i])

    answer = nums[0]
    for i in range(0, len(operator)):
        if operator[i] == "+":
            answer += nums[i+1]
        elif operator[i] == "-":
            answer -= nums[i + 1]
        elif operator[i] == "*":
            answer *= nums[i + 1]

    # return answer
    print(answer)
