## 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수

def solution(n):
    ## return을 할 정답 변수 설정
    answer = ''
    
    ## n 만큼 반복
    for i in range(n):
        ## 만약에 2로 나눈 나머지가 0이라면 (i가 짝수라면)
        if i % 2 == 0:
            ## answer 라는 변수에 '수'를 추가
            answer += '수'
        
        ## 아니라면(i가 홀수라면)
        else:
            ## answer 라는 변수에 '박'을 추가
            answer += '박'
    return answer