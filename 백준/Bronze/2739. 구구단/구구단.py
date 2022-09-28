## N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력
N = int(input())

## 1부터 9까지만 곱함
for i in range(9):
    ## N 은 문자열이기 때문에 int()로 정수변환
    result = int(N) * (i+1)
    print(N, '*', i+1, '=', result)