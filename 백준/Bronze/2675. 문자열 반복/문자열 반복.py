## 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램

## 테스트 케이스의 개수 T
T = int(input())

## 테스트 케이스 만큼 반복
for i in range(T):
    ## 반복 횟수 R, 문자열 S 를 문자열로 받기
    R, S = input().split()
    
    ## 문자열 S의 길이만큼 반복
    for j in range(len(S)):
        # print(j)

        ## 문자열의 요소에 반복횟수 R을 곱해주기 -> 공백없이 이어서
        print(str(S)[j] * int(R), end='')
    
    ## 한 번 출력하고 다음 출력은 다음 줄에서 결과값 출력
    print()