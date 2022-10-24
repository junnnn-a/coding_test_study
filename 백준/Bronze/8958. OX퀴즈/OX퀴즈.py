## OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램

test_case_len = int(input())
result = 0
count = 1

for i in range(test_case_len):
    quiz = input()
    
    for j in range(len(quiz)):
        if quiz[j] == 'O':
            result += count
            count += 1

        else:
            result += 0
            count = 1

    print(result)
    result = 0
    count = 1