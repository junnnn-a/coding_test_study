def solution(strings, n):
    string = []
    answer = []
    
    for i in strings:
        i = i[n]+i
        string.append(i)
        # answer.sort()
    string = sorted(string)
    for i in range(len(string)):
        answer.append(string[i][1:])
    
#     for i in answer:
#         answer.append(i[1:])
    
    return answer