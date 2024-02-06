m = int(input())
n = int(input())
weights = []
for i in range(n):
    weights.append(int(input()))
weights.sort()

boats = 0
i = 0
j = n - 1
while i <= j:
    if weights[i] + weights[j] <= m:
        i += 1
        j -= 1
    else:
        j -= 1
    boats += 1

print(boats)
