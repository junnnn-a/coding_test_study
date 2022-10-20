def solution(price, money, count):
    answer = 0
    
    for i in range(count):
        answer += price * (i+1)

    result = answer - money
    
    if result > 0 :
        return result
    else :
        return 0