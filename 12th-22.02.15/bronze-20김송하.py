def cycle(n):
    goal = n
    n1 = int(n//10)
    n2 = int(n%10)
    number = n1+n2
    n4 = int(number % 10)
    count = 1
    num = n2*10 + n4
    while num != goal:
        if num < 10:
            n1 = 0
            n2 = num
        else:
            n1 = int(num//10)
            n2 = int(num%10)
        number = n1 + n2
        if number < 10:
            n4 = int(number)
        else:
            n4 = int(number % 10)
        num = n2*10 + n4
        count+=1
    return count


n = int(input())
print(cycle(n))
