def solution(s):
    answer = True
    if len(s) == 4:
        try:
            s = int(s)
        except:
            answer = False
    elif len(s) == 6:
        try:
            s = int(s)
        except:
            answer = False
    else:
        answer = False
    return answer