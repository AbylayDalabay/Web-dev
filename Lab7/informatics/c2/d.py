n = int(input())
k = 2
while k != n:
    if k > n:
        print("NO")
        break
    k = k * 2
else:
    print("YES")