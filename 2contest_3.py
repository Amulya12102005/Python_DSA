t = int(input())
for p in range(t):
    n, m = map(int, input().split())
    for p in range(n):
        row = ""
        for k in range(m):
            row += str((p + k) % 2)
        print(row)