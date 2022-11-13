## 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균
## 과목의 갯수
number_of_subjects = int(input())

## 각 점수를 input으로 받는데 list에 int형으로 저장
score = (list(map(int, input().split())))

## score list 에 있는 최댓값 뽑기
max_score = max(score)
result = 0

## score list를 반복
for i in score:
    ## 이렇게 점수 계산을 한 결과의 평균을 반환
    result += i/max_score*100
print(result/len(score))