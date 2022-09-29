## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램

## 정수 A, B 가 들어온다면 계속해서 출력
while True:
    try:
        A , B = map(int, input().split())
    except:
        break
    print(A+B)