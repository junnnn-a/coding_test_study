## 어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램

C_score = input()
score = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
        'F' : 0.0}

print(score[C_score])

## 원래는 밑에처럼 일일히 조건문을 줘서 풀었다.
## 근데 좀 더 간결하게 풀고싶어서 딕셔너리 형태로 만들어보았다.

# C_score = input()
# if C_score == 'A+':
#     print('4.3')
# elif C_score == 'A0':
#     print('4.0')
# elif C_score == 'A-':
#     print('3.7')
# elif C_score == 'B+':
#     print('3.3')
# elif C_score == 'B0':
#     print('3.0')
# elif C_score == 'B-':
#     print('2.7')
# elif C_score == 'C+':
#     print('2.3')
# elif C_score == 'C0':
#     print('2.0')
# elif C_score == 'C-':
#     print('1.7')
# elif C_score == 'D+':
#     print('1.3')
# elif C_score == 'D0':
#     print('1.0')
# elif C_score == 'D-':
#     print('0.7')
# else:
#     print('0.0')
