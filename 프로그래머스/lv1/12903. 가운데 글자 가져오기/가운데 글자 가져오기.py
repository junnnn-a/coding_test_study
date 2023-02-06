def solution(s):
    if len(s) % 2 != 0:
        answer = len(s)//2
        return s[answer]
    else:
        answer = len(s)//2
        return s[answer-1]+s[answer]
    # print(answer)