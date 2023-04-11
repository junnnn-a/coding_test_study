## 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수

def solution(participant, completion):
    
    ## 일단 참가명단과 완주 명단을 비교하기 위해서 각 list를 정렬
    participant.sort()
    completion.sort()
    
    ## zip() 함수를 사용해서 명단끼리 연결
    for p, c in zip (participant, completion):
        ## 명단끼리 연결했는데 값이 다르면 반환
        if p != c :
            return p
    
    ## 완주 못한 선수를 구분해내기 위해서 맨 마지막 선수 출력
    return participant[-1]