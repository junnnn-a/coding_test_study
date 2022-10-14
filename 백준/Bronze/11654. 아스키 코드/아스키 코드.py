## 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램
## input() 받기
ASCII = input()

## input으로 받은 것의 type()이 int 숫자일 때는 
if type(ASCII)==int:
    ## chr()메서드를 사용하서 아스키코드값 출력
    print(chr(ASCII))

## input으로 받은 것이 type()이 str 숫자일 때는
else:
    ## ord()메서드를 사용해서 아스키코드값 출력
    print(ord(ASCII))