## 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램
## 단어 S 를 input으로 받아오기 -> 단어를 하나하나 리스트로 변환
S = list(input())

## 단어 S가 소문자로 이뤄져 있으니까 a-z까지의 알파벳을 리스트에 담아줌
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
## 단어 위치를 담아 둘 리스트 만들기
answer = []

## 알파벳(26) 리스트의 길이만큼 반복문 
for i in range(len(alphabet)):

    ## 만약에 알파벳이 S에 있다면
    if alphabet[i] in S:
        ## 리스트에다가 S에 해당 리스트를 추가
        answer.append(S.index(alphabet[i]))
    
    ## 알파벳이 S에 없다면 -1 을 리스트에 추가
    else:
        answer.append(-1)

    ## answer 리스트 값을 띄어쓰기로 출력
    print(answer[i], end=' ')
