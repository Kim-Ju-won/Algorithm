num = list(map(int, input().split()))

ascend = 0
descend = 0 

for i in range(1,len(num)):
    if num[i] > num[i-1] :
        ascend +=1
    else : 
        descend += 1

if ascend == len(num) -1:
    print("ascending")

if descend == len(num) -1 :
    print("descending")

if ascend > 0 and descend > 0 :
    print("mixed")
    