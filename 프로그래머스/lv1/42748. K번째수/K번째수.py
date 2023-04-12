## 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수

def solution(array, commands):
    answer = []
    
    ## commands가 조건 같은거니까 매개변수의 갯수만큼 반복
    for i in range(len(commands)):
        '''
        여기서 주의! 
        문제에서 2번째 5번째라고 하는거에서 1씩 빼줘서 계산해야함!
        why?
        -> 우리는 인덱스를 0부터 세기 때문에!
        '''
        
        ## array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬
        a = array[commands[i][0]-1 : commands[i][1]]
        a.sort()
        ## k번째에 있는 수를 구해서 answer 리스트에 추가한 후에 반환
        answer.append(a[commands[i][2]-1])
    return answer