## 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램
N = int(input())

## 5가 들어가면 1,2,3,4,5 가 출력되어야 하니까 print(i+1)을 해준다.
for i in range(N):
    print(i+1)