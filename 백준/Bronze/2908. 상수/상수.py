## 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램

A , B = input().split()
new_A = ''
new_B = ''
for i in range(2,-1,-1):
    # print(i)
    new_A += A[i]
    new_B += B[i]
# print(int(new_A) > int(new_B))

if (int(new_A) > int(new_B)) == True:
    print(new_A)
if (int(new_A) < int(new_B)) == True:
    print(new_B)

# for i in range(1, 5):
#     print(i)