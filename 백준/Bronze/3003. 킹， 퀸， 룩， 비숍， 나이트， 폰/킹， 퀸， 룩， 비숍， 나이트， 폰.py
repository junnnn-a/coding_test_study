orignal_chess = [1,1,2,2,2,8]
find_chess = map(int, input().split())
find_chess = list(find_chess)

for i in range(6):
    print(orignal_chess[i] - find_chess[i], end=' ')