t = int(input())
for a in range(t):
    n, k = map(int, input().split())
    casinos = []
    for b in range(n):
        l, r, real = map(int, input().split())
        casinos.append([l, r, real])

    casinos.sort()
    currentCoins = k
    visited = [0] * n
    idx = 0

    while True:
        maxValue = currentCoins
        indr = -1

        while idx < n and casinos[idx][0] <= currentCoins:
            l, r, real = casinos[idx]
            if real > maxValue and currentCoins <= r:
                maxValue = real
                indr = idx
            idx += 1

        if indr == -1:
            break

        visited[indr] = 1
        currentCoins = maxValue

    print(currentCoins)