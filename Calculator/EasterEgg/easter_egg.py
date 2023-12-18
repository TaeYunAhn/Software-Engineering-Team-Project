def easter_egg(answer):
    if answer == 7503:
        print("[EVENT] 안녕! 7503는 사용할 수 없는 숫자야")
        return True
    elif answer == 1015:
        print("[EVENT] 전북대 개교기념일입니다.")
        return True
    else:
        return None
