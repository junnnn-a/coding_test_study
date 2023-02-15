def solution(n):
    answer = 0
    # print(type(n))
    n = str(n)
    for i in range(len(n)):
        answer += int(n[i])
    
    # a = 'answer'
    # print(a[1])

    return answer
