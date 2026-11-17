n,m = map(int,input().split())
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True
x = False

if is_prime(n) and is_prime(m):
    consecutive = True

    for i in range(n + 1, m):
        if is_prime(i):
            consecutive = False
            break

    print("YES" if consecutive else "NO")
else:
    print("NO")