## 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램

## 변수와 리스트 만들기
mul = 1
answer = []

## 3개의 자연수를 받아서 바로 곱해서 변수에 저장
for i in range(3):
    mul *= int(input())

## 0부터 9까지 숫자가 몇 번씩 쓰였는지 체크! -> count() 함수 사용
for i in range(10):
    ## str 형이라서 전부다 문자형으로 변경해주기! 
    answer.append(str(mul).count(str(i)))
    print(answer[i])

'''
코드 간소화는 일단 다 작성한 후에 하는게 수월함!!
'''