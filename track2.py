#2063

N = int(input())
num = list(map(int, input().split()))
num.sort()
T = (N+1)/2
print(num[T])

