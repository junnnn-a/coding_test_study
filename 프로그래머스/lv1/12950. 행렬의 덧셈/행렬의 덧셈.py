def solution(arr1, arr2):
    hi = []
    bye = []
    for i in range(len(arr1)) :
        for j in range(len(arr1[i])) :
            hi.append(arr1[i][j] + arr2[i][j])
        bye.append(hi)
        hi = []
    return bye