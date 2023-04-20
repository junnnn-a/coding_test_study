def solution(s):
    answer = ''
    # print(s.split(' '))
    word = (s.lower()).split(' ')
    # print(word)
    for i in range(len(word)):
        for j in range(len(word[i])):
            if j % 2 == 0:
                answer += word[i][j].upper()
            else:
                answer+= word[i][j]
        answer += ' '
    return answer[ :-1]
