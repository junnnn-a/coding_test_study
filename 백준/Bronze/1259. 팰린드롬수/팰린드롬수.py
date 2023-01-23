## 각 줄마다 주어진 수가 팰린드롬수(어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어는 팰린드롬)면 'yes', 아니면 'no'를 출력하는 프로그램

while True:
    num = input()
    if num == '0':
        break

    if num == num[::-1]:
        print('yes')
    else:
        print('no')