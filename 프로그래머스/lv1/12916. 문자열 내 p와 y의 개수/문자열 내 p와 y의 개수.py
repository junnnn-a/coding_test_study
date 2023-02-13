def solution(s):
    answer = True
    
    ## 문자열 s 전체를 소문자로 변경해서 s_lower 이라는 변수에 저장
    s_lower = s.lower()
    
    ## 만약에 s_lower에 있는 'p'의 갯수와 'y'의 갯수가 같으면 answer 는 True
    if s_lower.count('p') == s_lower.count('y'):
        answer = True
    
    ## 갯수가 같지 않다면 answer 는 False
    else:
        answer = False

    return answer