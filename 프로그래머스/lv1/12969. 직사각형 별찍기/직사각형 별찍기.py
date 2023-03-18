## 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력
n, m = map(int, input().strip().split(' '))

## 별이 한 줄에 n개만큼 m줄이 필요함
for i in range(m):
    print('*'*n)