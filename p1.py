import itertools as it

v= range(0,18)
e= []

for i in v:
    for j in v:
        if j-i==6:
            e.append([i,j])
        elif j-i==1:
            e.append([i,j])

e.remove([5,6])
e.remove([11,12])

print(list(v))
print(e)

colors=range(0,4)
U=list(it.product(colors,repeat=(18)))

for i in range(0,len(U)):
    for j in range (0,len(e)):
        if U[i][e[j][0]]==U[i][e[j][1]]:
            U.remove(U[i])

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(len(U)) 