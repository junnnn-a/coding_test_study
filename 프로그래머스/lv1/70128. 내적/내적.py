## a와 b의 내적을 return 하도록 solution 함수

def solution(a, b):
    answer = 0
    
    ## a, b의 길이가 같으니까 배열의 길이만큼 반복
    for i in range(len(a)):
        ## 두 배열을 내적한 후 반환 (자릿수끼리 곱해서 answer에 더해주기)
        answer += a[i] * b[i]
        
    return answer