# 1989


T = int(input())
        
for t in range(1, T+1):
    w = input()
    if w == w[::-1]:
        print("#%d" %t, 1)
    else:
        print("#%d" %t, 0)
