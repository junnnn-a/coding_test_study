## 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수

def solution(s):
    answer = True
    
    ## 만약에 문자열 s의 길이가 4또는 6일 때만 해당 함수 실행
    if len(s) == 4 or len(s) == 6:
        
        ## 문자열 s에 int()를 씌워서 오류가 발생하면 False로 예외 처리
        try:
            s = int(s)
        except:
            answer = False
    
    ## 문자열 s 길이가 4또는 6이 아닌 모든 경우는 False
    else:
        answer = False
        
    return answer