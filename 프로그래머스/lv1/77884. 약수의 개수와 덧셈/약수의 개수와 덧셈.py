def solution(left, right):
    answer = 0
    divisor = []
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0 :
                divisor.append(j)
            # print(divisor)
        if len(divisor) %2 == 0:
            answer += j
        else:
            answer -= j
        divisor = []
    return answer