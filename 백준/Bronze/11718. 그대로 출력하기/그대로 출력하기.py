## 입력 받은 대로 출력하는 프로그램
## Ture이면 반복문이 계속해서 반복함
while True:
    ## 예외처리로 input이 안들어오면 멈추게 설정!
    try:
        input_output = input()

    except:
        break

    print(input_output)