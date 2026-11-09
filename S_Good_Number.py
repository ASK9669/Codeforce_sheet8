n, k = map(int, input().split())

count = 0

for i in range(n):
    a = input()

    good = True

    for j in range(k + 1):
        if str(j) not in a:
            good = False
            break

    if good:
        count += 1

print(count)