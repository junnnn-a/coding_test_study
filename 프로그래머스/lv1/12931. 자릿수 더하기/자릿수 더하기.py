## 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수

def solution(n):
    answer = 0
    # print(type(n))
    
    ## n이 자연수기 때문에 자릿수를 하나씩 더할려면 str() 형으로 바꿔줌
    n = str(n)
    
    ## n은 이제 문자열이니까 자릿수를 기준으로 수를 하나씩 뜯어서 answer에 더해주기(더해줄 때는 int()형으로 변경)
    for i in range(len(n)):
        answer += int(n[i])

    return answer
