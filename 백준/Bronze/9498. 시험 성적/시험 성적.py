## 시험점수를 받아서 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 
## 나머지 점수는 F를 출력하는 프로그램

score = int(input())

## 90 ~ 100 -> A
if score >= 90 and score <= 100:
    print('A')

## 80 ~ 89 -> B
elif score >= 80 and score < 90 :
    print('B')

## 70 ~ 79 -> C
elif score >= 70 and score < 80:
    print('C')

## 60 ~ 69 -> D
elif score >= 60 and score < 70:
    print('D')

## 59 ~ 0 -> F
else:
    print('F')