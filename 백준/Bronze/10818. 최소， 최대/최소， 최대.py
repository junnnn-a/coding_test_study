## N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램
N = int(input())

# numbers = [int(input()) for i in range(N)]    ## 이건 우리가 input 을 한 줄씩 받을 때 사용!

## 이건 우리가 input() 을 한 줄이 아니라 옆으로 띄어쓰기로 받을 때 (ex. 20 10 35 30 7)
numbers = list(map(int,  input().split()))

print(min(numbers), max(numbers))

'''
채점결과의 문제점 -> 시간이 많이 걸린 것 같음,,, (코테에서는 시간이 중요..ㅜ)
그래서 input()은 시간이 많이 필요로 하니까 담부터는 input() 대신에 sys.stdin.readline() 을 사용해야겠다!
sys 를 사용할 때는 import sys 해줘야함!

<바꾼코드>

import sys
N = int(input())
numbers = list(map(int,  sys.stdin.readline().split()))
print(min(numbers), max(numbers))

'''