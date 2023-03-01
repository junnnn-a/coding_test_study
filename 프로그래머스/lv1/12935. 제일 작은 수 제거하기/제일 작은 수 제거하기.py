## 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수

def solution(arr):
    answer = []
    
    ## 만약에 배열 arr의 길이가 1이라면 (배열에 값이 하나라면)
    if len(arr)==1:
        answer.append(-1)
    else:
        min_num = min(arr)
        # answer.append(1)
        arr.remove(min_num)
        answer = arr
    return answer