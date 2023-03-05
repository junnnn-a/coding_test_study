def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        # print(numbers[i])
        for j in range(i+1, len(numbers)):
            # print('i', numbers[i])
            # print('j', numbers[j])
            answer.append(numbers[i]+numbers[j])
            # print(answer)
    answer = list(set(answer))
    answer.sort()
    return answer