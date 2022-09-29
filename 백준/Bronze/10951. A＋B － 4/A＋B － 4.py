## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램

## 정수 A, B 가 들어온다면 계속해서 출력
while True:
    try:
        A , B = map(int, input().split())
    except:
        break
    print(A+B)

## try, except 를 넣어주지 않으니 코드가 계속 실행이 되어서 입력을 계속해서 받음
## EOF 즉 파일의 끝을 제대로 처리해야함!!! 
## 그래서 예외처리로 코드가 멈추도록 만들었음