## 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수

def solution(n, k):
    answer = (n * 12000) + (k*2000) - (n//10*2000)
    return answer