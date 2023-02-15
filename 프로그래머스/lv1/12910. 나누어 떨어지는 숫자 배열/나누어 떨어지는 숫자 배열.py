## array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수

def solution(arr, divisor):
    answer = []
    
    ## arr 리스트에 있는 수를 divisor로 나누어 떨어진다면 answer 리스트에 추가
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    ## 만약 divisor로 나눠지는 요소가 없으면 answer에 -1 을 추가
    if len(answer) == 0:
        answer.append(-1)
    
    ## answer을 오름차순으로 정렬해야해서 sorted() 내장함수를 사용해서 정렬 후 answer 반환
    return sorted(answer)