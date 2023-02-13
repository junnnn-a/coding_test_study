def solution(s):
    answer = True
    s_lower = s.lower()
    
    if s_lower.count('p') == s_lower.count('y'):
        answer = True
    else:
        answer = False

    return answer