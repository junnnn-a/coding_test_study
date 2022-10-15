## 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램
## 리스트 컴프리헨션으로 9개의 자연수를 리스트로 만들기
numbers = [int(input()) for i in range(9)]

## 리스트에서 최댓값 구하기
answer = max(numbers)

## 최댓값 출력
print(answer)
## 최댓값 index 를 출력 -> 근데 index는 0부터 시작이니까 1을 더해줘서 몇 번째 자리인지 출력~
print(numbers.index(answer)+1)