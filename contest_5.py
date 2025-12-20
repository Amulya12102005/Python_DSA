

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()

    case = x
    found = False

    for ops in range(6):
        if s in case:
            print(ops)
            found = True
            break
        case = case + case

    if not found:
        print(-1)
