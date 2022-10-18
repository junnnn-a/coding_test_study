## N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램

N = int(input())
numbers = input()
result = []
answer = 0

## N 개의 숫자가 공백으로 쓰여져있으니까 N 만큼 반복
for i in range(N):
    ## 문자열로 받은 input이 공백없이 들어오니까 0번째부터 i+1까지 잘라서 리스트에 저장
    result.append(numbers[i:i+1])
    
    ## 리스트에 각 요소를 저장한 것을 바탕으로 answer이라는 변수에 정수 형태로 더해주기
    answer += int(numbers[i])

print(answer)