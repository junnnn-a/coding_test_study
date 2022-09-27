## 좌표 x, y 2개를 받아 해당 좌표가 몇 사분면에 있는지를 출력하는 프로그램

# x, y = map(int, input().split())
## 한 줄씩 입력 받기
x = int(input())
y = int(input())

## 1사분면
if x > 0 and y > 0 :
    print('1')

## 2사분면
elif x < 0 and y > 0 :
    print('2')

## 3사분면
elif x < 0 and y < 0 :
    print('3')

## 4사분면
elif x > 0 and y < 0 :
    print('4')

## 추가 x, y 가 0이거나 나머지 값일 때! 
else:
    print('None')