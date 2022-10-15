## N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램

N = int(input())

# numbers = [int(input()) for i in range(N)]    ## 이건 우리가 input 을 한 줄씩 받을 때 사용!

## 이건 우리가 input() 을 한 줄이 아니라 옆으로 띄어쓰기로 받을 때 (ex. 20 10 35 30 7)
numbers = list(map(int,  input().split()))

print(min(numbers), max(numbers))