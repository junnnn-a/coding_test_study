## 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램
N = int(input())

## 자연수 N부터 1까지 출력(역순)
for i in range(N, 0, -1):
    print(i)