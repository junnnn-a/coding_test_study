## 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 함수

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