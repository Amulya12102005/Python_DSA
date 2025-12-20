t = int(input())

for u in range(t):
    num = int(input())
    string = input()

    if num != 5:
        print("NO")
        continue

    if sorted(string) == sorted("Timur"):
        print("YES")
    else:
        print("NO")
