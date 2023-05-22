## 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수

def solution(angle):

    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle == 180:
        return 4
    else:
        return 3
    
    
