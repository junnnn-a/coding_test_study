## N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램
## N*M 크기니까 input으로 행렬 크기 받기
N, M = map(int, input().split())

## N*M 행렬을 각각 따로 만들기
A = []
B = []

## A 행렬 만들기
for i in range(N):
    A.append(list(map(int, input().split())))

## B 행렬 만들기
for i in range(N):
    B.append(list(map(int, input().split())))

## 만들어진 A 행렬에다가 B 행렬 더하기
for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

        ## 더해진 A 행렬 요소별로 묶어서 출력
        print(A[i][j], end=' ')
    print()

'''
처음에 2번째 for 문을 for i in range(M): 
M이라고 작성을 해서 계속 런타임 오류가 났다.. 위에 A 행렬 만들기와 같이 행으로 
반복문을 돌려야함~!~

그리고 맨 밑에 이중 반복문은 행과 열을 잘 분리해서 반복문 범위를 설정해야함!
'''