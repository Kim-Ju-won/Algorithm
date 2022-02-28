def ans(n):
    num = 0
    while n >= 0:
        if n % 5 == 0:
            return num+(n//5)
        n-=3
        num+=1
    return -1

n = int(input())
print(ans(n))