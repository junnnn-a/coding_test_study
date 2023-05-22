## num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수

def solution(num1, num2):
    answer = num1/num2
    
    return int(answer*1000)