def solution(arr1, arr2):
    array_1 = []
    array_2 = []
    for i in range(len(arr1)) :
        for j in range(len(arr1[i])) :
            array_1.append(arr1[i][j] + arr2[i][j])
        array_2.append(array_1)
        array_1 = []
    return array_2