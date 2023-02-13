n, m = map(int, input().strip().split(' '))
for i in range(m):
    star = ""
    for j in range(n):
        star += '*'
    print(star)
