## 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수

def solution(arr):
    answer = []
    
    ## 만약에 배열 arr의 길이가 1이라면 (배열에 값이 하나라면)
    if len(arr)==1:
        ## 바로 -1을 리턴
        answer.append(-1)
    
    ## 배열 arr의 길이가 1이 아닌 경우
    else:
        ## 배열 arr에 있는 최솟값을 뽑아서 그 값을 제거하고 새로운 리스트 리턴
        min_num = min(arr)
        arr.remove(min_num)
        answer = arr
        
    return answer