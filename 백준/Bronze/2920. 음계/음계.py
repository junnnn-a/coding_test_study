## 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램
## input 으로 값을 8개 받아 list 로 저장
scale = list(map(int, input().split()))

## 만약에 scale(input 으로 받은 list) 이 오름차순으로 담긴 리스트라면
if scale == [1, 2, 3, 4, 5, 6, 7, 8] :
    ## ascending 을 출력
    print('ascending')

## 만약게 scale 이 내림차순으로 담긴 리스트라면
elif scale == [8, 7, 6, 5, 4, 3, 2, 1]:
    ## descending 출력
    print('descending')

## 그 외에는
else:
    ## mixed 출력
    print('mixed')