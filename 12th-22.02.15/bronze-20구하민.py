n = input()

if int(n)//10 == 0 : 
    n = '0'+ n
    
num = n 
result = ''
count = 0

while True :
    if n == result : break
    result = num[-1]+str((int(num[0])+int(num[1]))%10)
    num = result
    count += 1
print(count)
