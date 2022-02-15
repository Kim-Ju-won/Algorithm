# 함수
def max_stair(S):
    n = len(S)
    # O(n)
    DP_max =[ 0 for _ in range(n)]
    check = [ 2 for _ in range(n)]

    # O(n)
    for i in range(n-1,-1,-1):
        if i == n-1 :
            DP_max[i] = S[i]
            check[i] = 1
        elif i == n-2 :
            DP_max[i] = S[i+1] + S[i]
            check[i] = 0
        else:
            if check[i+2] == 2:  
                if check[i+3] == 2:
                    DP_max[i]= max(DP_max[i+3]+S[i+1]+S[i+2])
                    check[i] = 0
                else : 
                    DP_max[i]= DP_max[i+1] + S[i]
                    check[i] = 0
            elif check[i+2] == 1 : 
                DP_max[i] = max(DP_max[i+2] + S[i+1], DP_max[i+2] + S[i])
                if DP_max[i+2] + S[i+1] == DP_max[i] :
                    check[i]=2
                if DP_max[i+2] + S[i] == DP_max[i] :
                    check[i]=1
            else:
                if check[i+1] == 1 : 
                    DP_max[i]= max(DP_max[i+1] + S[i],  DP_max[i+2] + S[i])
                    if DP_max[i]== DP_max[i+2] + S[i]:
                        check[i] = 1
                    if DP_max[i]== DP_max[i+1] + S[i]:
                        check[i] = 0
                else :
                    DP_max[i]= DP_max[i+2] + S[i]
                    check[i] = 1
    print(DP_max[0])
# 입력
n = int(input())
Stair =[]
for i in range(n):
    Stair.append(int(input()))
# 출력
max_stair(Stair)