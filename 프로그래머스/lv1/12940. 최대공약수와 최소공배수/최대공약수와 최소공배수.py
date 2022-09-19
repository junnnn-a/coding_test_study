def solution(n, m): # 유클리드 호제법
    answer = []
    a = max(n, m)
    b = min(n, m)
    
    while b != 0:
        r = a%b
        a = b
        b = r
    answer = [a, n*m//a]
    return answer