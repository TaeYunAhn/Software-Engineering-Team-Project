# 로그는 배열
log=["1+1=1", "1+2=3"]
# 이와 같은 형식으로 담겨 있다고 가정
# 테스트 확인 후 주석처리

def print_log():
    if log:
        for entry in log:
            print(entry)
    else:
        print("NO LOG!")