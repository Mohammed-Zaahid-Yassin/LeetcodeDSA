r, c = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(r)]

for j in range(c):
    row = []
    for i in range(r):
        row.append(m[i][j])
    print(*row)
