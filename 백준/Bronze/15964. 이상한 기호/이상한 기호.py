## 정수 A, B가 주어지면 A＠B를 계산하는 프로그램
## 문제 분류가 함수여서 함수로 만들어서 출력하기!!
def math():
    A, B = map(int, input().split())
    return (A+B)*(A-B)

print(math())