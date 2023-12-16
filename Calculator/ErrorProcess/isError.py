def is_error(data):
    flag = 1    # 숫자나 연산자 중복 확인

    num_count = 0
    operator_count = 0

    operators = []

    # 숫자나 연산자가 연속으로 두 개 이상 들어온 경우
    for i in range(0, len(data)):
        try:
            int(data[i])
            num_count += 1
            if flag == 1:
                flag = 0
                continue
            else:
                return False
        except ValueError:
            # 더하기, 빼기, 곱하기 이외의 연산자 확인
            if data[i] not in ['+', '-', '*']:
                return False

            operator_count += 1
            operators.append(data[i])
            if flag == 0:
                flag = 1
                continue
            else:
                return False

    # 연산자와 숫자의 개수가 알맞게 들어오지 않는 경우
    if num_count != operator_count + 1:
        return False

    # 서로 다른 연산자가 들어온 경우
    for i in range(1, len(operators)):
        if operators[i-1] != operators[i]:
            return False

    return True

def is_factorial_error(data):
    # 입력된 데이터가 정확히 두 개의 요소를 가지는지 확인
    if len(data) != 2:
        return False

    number, symbol = data

    # 첫 번째 요소가 0 이상의 정수인지 확인
    if not number.isdigit() or int(number) < 0:
        return False

    # 두 번째 요소가 '!' 기호인지 확인
    if symbol != '!':
        return False

    return True
