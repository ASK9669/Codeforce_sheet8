n = int(input())

x = "maybe"

previous = []

for i in range(n):
    a, b = map(int, input().split())

    if a != b:
        x = "rated"

    previous.append(a)

if x != "rated":
    for i in range(n - 1):
        if previous[i] < previous[i + 1]:
            x = "unrated"
            break
    else:
        x = "maybe"

print(x)