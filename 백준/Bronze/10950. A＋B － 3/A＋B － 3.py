## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
T = int(input())

## 입력받은 T 만큼 반복
for i in range(T):
    ## A, B 를 입력하고 합을 print
    A, B = map(int, input().split())
    print(A+B)