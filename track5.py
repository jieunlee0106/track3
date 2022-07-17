


T = int(input())
 
for tc in range(T):
    data = ''
    N = int(input())
    for _ in range(N):
        chr, num = map(str, input().split())
        data += chr * int(num)
 
    print('#{}'.format(tc+1))
    for i in range(0, len(data), 10):
        print(data[i:i+10])




T = int(input())
 
for t in range(T):
    result = ''
    N = int(input())
    for _ in range(N):
        alp, num = map(str, input().split())
        result += alp * int(num)
 
    print('#{}'.format(t+1))
    for i in range(0, len(result), 10):
        print(result[i:i+10])


