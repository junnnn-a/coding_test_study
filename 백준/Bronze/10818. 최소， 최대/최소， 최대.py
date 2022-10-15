## N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램

N = int(input())

# numbers = [int(input()) for i in range(N)]
numbers = list(map(int,  input().split()))

print(min(numbers), max(numbers))