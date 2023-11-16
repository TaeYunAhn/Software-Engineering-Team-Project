def operation(data):
    nums = []
    operator = []

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

    return answer
