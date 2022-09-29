## 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램

N, X = map(int, input().split())
A = list(map(int,input().split()))

for i in A:
    if i<X:
        print(i, end=' ')

## 이 풀이를 하면서 굳이 N을 받을 이유가 있나..? 라는 생각을 했음

##------------------------------------------------------------------------------
## 그래서 N을 활용해서 다시 짠 코드
N, X = map(int, input().split())
A = list(map(int,input().split()))

for i in range(N):
    if A[i] < X :
        print(A[i], end=' ')