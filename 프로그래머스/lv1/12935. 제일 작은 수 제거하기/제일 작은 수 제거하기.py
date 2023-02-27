def solution(arr):
    answer = []
    
    if len(arr)==1:
        answer.append(-1)
    else:
        min_num = min(arr)
        # answer.append(1)
        arr.remove(min_num)
        answer = arr
    return answer