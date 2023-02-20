def solution(n):
    answer = []
    n = str(n)
    for i in n:
        answer.append(i)
        answer.sort()
    return int(''.join(reversed(answer)))