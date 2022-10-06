## 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램

submitter = [int(input()) for i in range(28)]
all_class = [i+1 for i in range(30)]

for i in all_class:
    if i not in submitter:
        print(i)