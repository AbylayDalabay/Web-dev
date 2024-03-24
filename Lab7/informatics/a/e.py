v = int(input())
t = int(input())
x = ((v*t+1))%109
if x == 0:
    print(108)
else:
    if x < 0:
        x = x + 109
    print(x-1)