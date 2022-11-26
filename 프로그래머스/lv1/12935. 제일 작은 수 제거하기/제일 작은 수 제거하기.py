def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
        
    else:
        # arr_1 = sorted(arr)
        # print(min(arr))
        arr.remove(min(arr))
        # print(arr)
        for i in arr:
            answer.append(i)
                
    return answer
