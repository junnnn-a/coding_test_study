## 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램

## (x, y)는 지금 현재 있는 곳 , 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)
x, y, w, h = map(int, input().split())
answer = []

'''
리스트에 처음에는 append 로 해서 요소를 한 개씩 추가했지만
extend를 통해서 한 번에 리스트에 요소를 추가할 수 있다!
'''
# answer.append(x)
# answer.append(w-x)
# answer.append(y)
# answer.append(h-y)

## 직사각형 경계선까지 가는 최단 거리기 때문에 가능성 4가지를 다 리스트에 추가 후 최솟값 찾기
answer.extend([x, w-x, y, h-y])
print(min(answer))