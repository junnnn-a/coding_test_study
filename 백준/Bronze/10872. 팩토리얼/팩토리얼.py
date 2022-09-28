## 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램
N = int(input())
answer = 1

## answer 이라는 변수에 i+1 즉, 1부터 N까지 곱함
for i in range(N):
    answer *= i+1

print(answer)