n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) == sum(b):
    print("Yes")
else:
    print("No") 