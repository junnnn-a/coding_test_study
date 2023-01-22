mul = 1
answer = []

for i in range(3):
    mul *= int(input())

for i in range(10):
    answer.append(str(mul).count(str(i)))
    print(answer[i])