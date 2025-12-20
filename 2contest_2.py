t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    digits = []
    letters = []

    valid = True
    password = False

    for ch in s:
        if ch.isdigit():
            if password:
                valid = False
            digits.append(ch)
        else:
            password = True
            letters.append(ch)


    if digits != sorted(digits):
        valid = False
    if letters != sorted(letters):
        valid = False

    if valid:
        print("YES")
    else:
        print("NO")

