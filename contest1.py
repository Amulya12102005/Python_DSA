n = int(input())
for i in range(n):
    text = input()
    length = len(text)

    if length > 10:
        print(text[0] + str(length-2) + text[-1])
    else:
        print(text)