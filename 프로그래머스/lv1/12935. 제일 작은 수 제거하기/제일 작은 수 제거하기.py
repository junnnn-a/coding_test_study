def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
        
    else:
        # arr_1 = sorted(arr)
        # print(min(arr))
        arr.remove(min(arr))
        # print(arr)
        # del arr_1[0]
        for i in arr:
            # if i in arr_1:
            answer.append(i)
                
    return answer
