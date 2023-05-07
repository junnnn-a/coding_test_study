## 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하는 함수

def solution(strings, n):
    string = []
    answer = []
    
    ## strings 의 요소를 하나씩 들고와서 n번째 인덱스의 문자를 요소 맨 앞에 붙히기
    for i in strings:
        i = i[n]+i
        string.append(i)
    
    ## 그 후에 정렬
    string = sorted(string)
    
    ## 이제 해당 인덱스의 문자의 요소를 붙힌 거를 떼서 answer 리스트에 추가
    for i in range(len(string)):
        answer.append(string[i][1:])
    
    return answer