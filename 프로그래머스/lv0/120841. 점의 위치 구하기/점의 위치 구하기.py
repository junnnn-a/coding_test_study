## 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수

def solution(dot):
    
    if dot[0]>0 and dot[1]>0:
        return 1
    
    elif dot[0]<0 and dot[1]>0:
        return 2
    
    elif dot[0]<0 and dot[1]<0:
        return 3
    
    else:
        return 4