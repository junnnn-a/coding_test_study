## N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램
N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

        print(A[i][j], end=' ')
    print()