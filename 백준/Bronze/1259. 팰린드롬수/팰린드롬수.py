## 각 줄마다 주어진 수가 팰린드롬수(어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어는 팰린드롬)면 'yes', 아니면 'no'를 출력하는 프로그램

## 입력은 여러개의 테스트케이스로 이뤄져 있으니까 while 문 사용
while True:
    num = input()
    ## input 으로 0이 들어오면 while 문 멈추기
    if num == '0':
        break
    
    ## num[::-1] 이게 문자열을 뒤집는거! 
    ## 원래 num 과 뒤집었을 때 같으면 yes 를 출력! 
    ## 만약에 int 형으로 받아서 출력하려면 int(str(num[::-1])) 이런식으로 작성하면 될 듯??
    if num == num[::-1]:
        print('yes')

    else:
        print('no')