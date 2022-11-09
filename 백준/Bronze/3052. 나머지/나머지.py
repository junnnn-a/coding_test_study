## 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램
## 수 10개를 입력으로 받은 다음 리스트로 저장 -> 리스트 컴프리헨션
number = [int(input()) for i in range(10)]
answer = []

## i 가 number인 리스트로 반복
for i in number:
    ## 각각 number 를 42로 나눠서 나머지 빈 리스트에 추가
    answer.append(i%42)

## 중복제거를 위해서 set()을 해주고 갯수를 출력
print(len(set(answer)))