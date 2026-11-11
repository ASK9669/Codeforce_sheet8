s = input()
s1 = []

for i in range(len(s)):
    if s[i] != "+":
        s1.append(s[i])

s1.sort()

n = ""

for i in range(len(s1)):
    n += s1[i]

    if i != len(s1) - 1:
        n += "+"

print(n)