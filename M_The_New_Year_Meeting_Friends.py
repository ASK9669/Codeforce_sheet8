x1, x2, x3 = map(int, input().split())

s = sorted([x1, x2, x3])

meeting = s[1]

distance = abs(x1 - meeting) + abs(x2 - meeting) + abs(x3 - meeting)

print(distance)