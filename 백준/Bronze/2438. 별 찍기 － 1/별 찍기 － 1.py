## 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

N = int(input())

## 총 N 번이 반복할 것!!
for i in range(N):
    ## i 가 한 번 반복할 때 j가 실행 (이중 for문)
    for j in range(i+1):
        ## 이중 반복문이 돌면서 첫 째 줄에는 별 1개, 두 번째 줄에는 2개로 증가하는 형태!
        print('*', end='')
    print()