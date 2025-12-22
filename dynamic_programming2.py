def fib(n):
    dp=[-1]*3
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i%3]=dp[(i-1)%3]+dp[(i-2)%3]
    return dp[n%3]
print(fib(4))