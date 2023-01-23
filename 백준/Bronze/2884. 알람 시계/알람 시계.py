## 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법(45분 일찍 알람 설정하기)을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램

H , M = map(int, input().split())

## 분이 45보다 크거나 같은 경우에는 그냥 45를 빼준다.
if M >= 45 :
    print(H , M-45)

## 분이 45보다 작은 경우에는 M에 60을 더한 후에 45를 빼준다.
else:
    ## 근데 시간이 0시일 수 있으니까 그럴 경우에는 그냥 23시를 출력
    if H < 1 :
        print(23, (M+60)-45)
    else:
        print(H-1, (M+60)-45)