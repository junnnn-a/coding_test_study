## 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램
## 영어 대소문자가 섞여 있는 단어를 input()으로 받기
word = input()
answer = ''

## 문자열의 길이만큼 반복문
for i in range(len(word)):
    ## 문자열이 대문자라면 (대문자인거 확인하는 메서드 .isupper() -> bool 형)
    if word[i].isupper() == True:
        ## 소문자로 바꿔서 answer 변수에 저장
        answer += word[i].lower()
    
    ## 문자열이 소문자라면 (소문자인거 확인하는 메서드 .islower() -> bool 형)
    else:
        ## 대문자로 바꿔서 변수에 저장
        answer += word[i].upper()
    
print(answer)