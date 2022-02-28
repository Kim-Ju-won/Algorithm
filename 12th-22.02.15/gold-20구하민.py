def solve(x, y) : 
    dis = y-x
    k = 1
    count = 0
    while dis > 0 : 
        if k*2 <= dis : 
            dis -= k*2
            k += 1
            count += 2
        elif k <= dis : 
            dis -= k
            count += 1
        else : 
            dis = 0
            count += 1
    return count
        

n = int(input())

for _ in range(n) : 
    x, y = map(int, input().split())
    print(solve(x, y))
