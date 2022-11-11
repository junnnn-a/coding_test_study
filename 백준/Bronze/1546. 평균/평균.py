## 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균

number_of_subjects = int(input())

score = (list(map(int, input().split())))

max_score = max(score)

result = 0

for i in score:
    result += i/max_score*100
    # print(result)
print(result/len(score))
# print(50/70*100)