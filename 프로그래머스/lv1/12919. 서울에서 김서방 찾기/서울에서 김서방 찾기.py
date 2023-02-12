## String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수

def solution(seoul):
    answer = 0
    ## seoul 리스트의 길이만큼 반복 -> 나중에 인덱스 값을 저장하기 위해서 리스트 길이만큼 반복~
    for i in range(len(seoul)):

        ## 만약에 리스트에 'Kim'이라는 문자열이 있으면 그 해당 인덱스를 answer에 저장
        if seoul[i] == 'Kim':
            answer += i
    
    ## 저장 된 index 수를 가지고 원하는 답 출력
    return "김서방은 " + str(answer) + "에 있다"