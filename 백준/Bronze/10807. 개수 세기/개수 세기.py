## 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램

N = int(input())
A = list(map(int, input().split()))
v = int(input())

## count 를 사용하여 A 에 있는 v 의 갯수 세기
answer = A.count(v)
print(answer)