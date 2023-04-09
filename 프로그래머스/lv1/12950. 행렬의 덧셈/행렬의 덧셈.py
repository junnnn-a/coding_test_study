## 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수

def solution(arr1, arr2):
    
    ## arr1과 arr2의 길이는 동일하니까 그 길이만큼 반복
    for i in range(len(arr1)):
        ## 전체 길이 말고 그 안에 원소의 길이만큼 반복
        for j in range(len(arr1[0])):
            
            ## 새로운 배열을 만들기 보다는 그냥 arr1 배열에 arr2 배열의 원소들을 더해주고 반환
            arr1[i][j] += arr2[i][j]
            
    return arr1