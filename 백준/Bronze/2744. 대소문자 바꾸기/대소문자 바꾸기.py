## 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램

word = input()
answer = ''
for i in range(len(word)):
    if word[i].isupper() == True:
        answer += word[i].lower()
    
    else:
        answer += word[i].upper()
    
print(answer)