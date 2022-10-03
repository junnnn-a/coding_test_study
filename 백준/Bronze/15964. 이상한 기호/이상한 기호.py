## 정수 A, B가 주어지면 A＠B를 계산하는 프로그램

A, B = map(int, input().split())

def math(A, B):
    return (A+B)*(A-B)

print(math(A,B))