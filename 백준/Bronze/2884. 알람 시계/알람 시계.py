H , M = map(int, input().split())

if M >= 45 :
    print(H , M-45)

else:
    if H < 1 :
        print(23, (M+60)-45)
    else:
        print(H-1, (M+60)-45)