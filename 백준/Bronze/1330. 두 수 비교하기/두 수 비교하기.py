## A, B 를 정수로 받아 값을 비교하는 프로그램
A, B = map(int, input().split())

## 조건1. A가 B보다 크면 '>'를 출력
if A > B :
    print('>')

## 조건2. A가 B보다 작으면 '<'를 출력
elif A < B :
    print('<')

## 조건 3. 이 외에는 (A와 B가 같은 경우) '==' 를 출력
else :
    print('==')