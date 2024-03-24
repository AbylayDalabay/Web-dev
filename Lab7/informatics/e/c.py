num = int(input())
inp = input().split()
print(len([x for x in inp if int(x) > 0]))
