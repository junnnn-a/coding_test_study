## 단어 s의 가운데 글자를 반환하는 함수

def solution(s):

    ## 단어 s가 홀수일 때
    if len(s) % 2 != 0:
        ## 길이를 2로 나눠서 그 해당 index를 반환
        answer = len(s)//2
        return s[answer]
    
    ## 단어 s가 짝수일 때는 가운데 두 글자를 반환
    else:
        ## 길이를 2로 나눠서 해당 index와 그 전 글자까지 함께 반환
        answer = len(s)//2
        ## 문자열 2개를 ',' 로 이으면 공백이 포함되지만 '+' 로 이으면 공백 없이 이어진다!
        return s[answer-1]+s[answer]
    # print(answer)