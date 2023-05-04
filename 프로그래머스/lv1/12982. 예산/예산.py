def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        
        if budget == 0:
            answer += i+1
            break
            
        elif budget < 0:
            print(i)
            answer += i
            break
    
    if budget > 0:
        answer += len(d)
    
    return answer