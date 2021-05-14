def check_number(a, b, c):
    for i in range(b, a-1):
        if an[i] == an[i - 1]:
            an.insert(an.index(b), c)
    return an




a = int(input())
an = []
for i in range(a):
    an.append(i)

b = int(input())
c = int(input())
print(check_number(a, b, c))