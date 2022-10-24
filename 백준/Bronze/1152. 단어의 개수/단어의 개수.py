## 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램

## 공백으로 이뤄진 문자열을 list 로 받음 (띄어쓰기 기준으로 나눠서 저장)
english_sentence = list(input().split())

## 공백을 기준으로 나눠서 list 에 저장을 했기 때문에 단어의 갯수는 list의 길이와 같음
print(len(english_sentence))