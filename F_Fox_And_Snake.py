n, m = map(int, input().split())
x = m-1
y = 1
for i in range(n):
    if i % 2 == 0:
        print("#" * m)
    else:
        print("." * x + "#" if y == 1 else "#" + "." * x)
        y = 1 - y