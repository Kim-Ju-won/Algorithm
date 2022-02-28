def sugar(n):
    a = 0
    for i in range(n//3+1):#5의 개수 최대 ->1,2
        for j in range(n//5+1):
            if 3*i + 5*j == n:
                a += (i+j)
                print(a)
                return                
    print(-1)

n = int(input())
sugar(n)

# 5*a + 3*b = n

# 0 <= a <= n//5, 0 <= b <= n//3
# 3 5 6 8 9 10 11 12 13 14 
