n = int(input())
a = list(map(int, input().split()))
for i in range((n+1)//2):
    a[i], a[n-i-1] = a[n-i-1], a[i]
print(*a)
