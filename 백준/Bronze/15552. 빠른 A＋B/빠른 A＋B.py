## 빠른 입출력!

## sys 모듈은 파이썬 인터프리터를 제어할 수 있는 방법을 제공해줌
import sys
T = int(input())

for i in range(T):
    ## 여기서 input()으로 받는게 아니라 sys.stdin.readline()으로 받아줌~
    ## 그래야 시간초과 되지 않고 더 빠르게 출력 가능함
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)