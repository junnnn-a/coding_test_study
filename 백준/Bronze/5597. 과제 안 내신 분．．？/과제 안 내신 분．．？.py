## 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램

## 과제 제출을 한 학생들을 모두 Input으로 받아서 리스트로 저장 -> int 형으로 저장
submitter = [int(input()) for i in range(28)]
## 전체 학생을 리스트로 저장 -> int형으로 저장
all_class = [i+1 for i in range(30)]

## 전체 학생리스트에서 과제 제출 학생 리스트에 없는 학생만 출력
for i in all_class:
    if i not in submitter:
        print(i)