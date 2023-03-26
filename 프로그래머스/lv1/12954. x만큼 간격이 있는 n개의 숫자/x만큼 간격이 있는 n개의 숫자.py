def solution(x, n):
    answer = []
    
    # for i in range(2, 11, 2):

    if x > 0:
        for i in range(x, x*n+1, x):
            answer.append(i)
    elif x < 0:
        for i in range(x, x*n-1, x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(0)
        
    return answer