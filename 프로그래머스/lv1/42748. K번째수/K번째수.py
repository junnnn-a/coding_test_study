def solution(array, commands):
    answer = []
    
    # print(array[0:3])
    
    for j in range(len(commands)):
        for i in range(len(array)):
            array_crop = array[commands[j][0]-1 : commands[j][1]]
        array_crop.sort()
        # print(array_crop)
        # print(array_crop[0])
        
        answer.append(array_crop[commands[j][2]-1])
    
    return answer