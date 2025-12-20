t = int(input())
for i in range(t):
    a, b = map(str,input().split())

    word1 = b[0] + a[1:]
    word2 = a[0] + b[1:]

    print(word1, word2)

