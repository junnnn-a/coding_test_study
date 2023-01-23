## 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하는 프로그램

## 입력이 여러개로 들어오고 0 0 0이 들어오면 멈춤
while True:
    ## 삼각형 3변을 변수에 저장하는데 sorted라는 함수를 써서 정렬을 해줌 -> 빗변이 뭔지 알아내기 위해서!
    A, B, C = sorted(map(int, input().split()))
    num = []
    if A==0 and B==0 and C==0:
        break
    
    ## num 이라는 list에 제곱값 한 번에 저장
    num.extend([A**2, B**2, C**2])
    
    ## 길이가 짧은 두변 제곱의 합이랑 빗변의 제곱이 같으면 직각삼각형이 맞다는 'right'를 출력
    if (num[0] + num[1]) == num[2]:
        print('right')
    else:
        print('wrong')