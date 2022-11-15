## 검증수를 출력하는 프로그램
## 문제 분류가 함수라서 함수로 만들기!!
def verifications():

    ## 입력값 5개 받아서 list로 저장
    numbers_list = list(map(int, input().split()))
    hap = 0

    ## 각 자릿수의 제곱의 합 구하기ㅣ
    for i in range(len(numbers_list)):
        hap += int(numbers_list[i])**2
    
    ## 합을 10으로 나눠서 나머지를 출력하기
    answer = hap % 10
    return answer
print(verifications())