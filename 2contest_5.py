t = int(input())

for i in range(t):
    x,y,z = map(int, input().split())

    if x+y>=10 or x+z>=10 or y+z>=10:
        print("YES")
    else:
        print("NO")
