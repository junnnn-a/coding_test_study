## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램

while True:
    A, B = map(int, input().split())
    ## A와 B 가 0 0 으로 들어오게 되면 프로그램이 멈춘다.
    if A == 0 and B == 0 :
        break
    print(A+B)