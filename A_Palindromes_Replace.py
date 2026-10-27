
s = list(input())

l = 0
r = len(s) - 1

while l < r:
    if s[l] == '?' and s[r] == '?':
        s[l] = 'a'
        s[r] = 'a'
    elif s[l] == '?':
        s[l] = s[r]
    elif s[r] == '?':
        s[r] = s[l]
    elif s[l] != s[r]:
        print(-1)
        break

    l += 1
    r -= 1
else:
    if s[l] == '?':
        s[l] = 'a'
    print(''.join(s))
ini