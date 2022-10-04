## 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램
T = int(input())

## 리스트 컴프리헨션으로 한 줄씩 input()값 받기! -> int, float등 아무것도 조건을 안줘서 문자열로 받음
string = [input() for _ in range(T)]
## string의 길이만큼 반복하는데 문자열의 맨 앞글자와 뒷글자를 출력하기
for i in range(len(string)):
    print(string[i][0]+string[i][-1])