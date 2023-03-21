## 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주는 함수

def solution(n):
    answer = []
    
    ## 정수 n을 문자열로 변경 -> 수를 하나하나 떼서 정렬하기 위해서
    n = str(n)
    
    ## 문자열을 반복할 때 자릿수를 떼어서 리스트에 추가 후 정렬
    for i in n:
        answer.append(i)
        answer.sort()
    
    ## 정렬 된 리스트를 거꾸로 나열해서 문자열로 변경 후 다시 정수로 return
    return int(''.join(reversed(answer)))