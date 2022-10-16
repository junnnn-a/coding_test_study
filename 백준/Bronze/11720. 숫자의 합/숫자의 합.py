## N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램

N = int(input())
numbers = input()
result = []
answer = 0

for i in range(N):
    result.append(numbers[i:i+1])

    answer += int(numbers[i])

print(answer)