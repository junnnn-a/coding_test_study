## OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램
## 일단 테스트 케이스 갯수를 input으로 받기
test_case_len = int(input())

## 점수를 더할 변수 설정
result = 0
## 맞는 'O' 가 여러개가 들어오면 점수를 1점씩 더 더해줘야해서 변수 생성
count = 1

## 테스트 케이스 갯수만큼 반복
for i in range(test_case_len):
    ## OX 퀴즈의 결과를 input으로 받기
    quiz = input()
    
    ## quiz의 길이만큼 반복
    for j in range(len(quiz)):
        ## quiz 가 'O' 라면
        if quiz[j] == 'O':
            ## 점수에다가 count 를 더해주기 -> 그리고 다시 맞으면 count 에다가 1씩 더해가면서 점수를 2점 3점 더해주기
            result += count
            count += 1

        ## quiz 가 'X' 라면
        else:
            ## 점수에다가 0점을 더해주고 -> count는 다시 초기화
            result += 0
            count = 1

    ## 한 번 quiz를 받아서 결과값을 내면 다시 변수들 초기화
    print(result)
    result = 0
    count = 1