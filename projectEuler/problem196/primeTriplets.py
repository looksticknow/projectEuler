from sympy import isprime

def findStart_Num(n):
    for i in range(1,n+1):
        primeNumber = int((0.5*i**2) - (0.5*i) + 1)
    return primeNumber


def SumTriplet(n, pfor, p, petter):
    rangeStop_pfor = findStart_Num(n-1)+(n-1)
    rangeStop_p = (findStart_Num(n)+n)
    rangeStop_petter = (findStart_Num(n+1)+(n-1))+2

    for i in range(findStart_Num(n-1),rangeStop_pfor):
        pfor.append(i)

    for i in range(findStart_Num(n),rangeStop_p):
        p.append(i)

    for i in range(findStart_Num(n+1),rangeStop_petter):
        petter.append(i)

pMin = []
p = []
pMax = []
pMin_index = []
p_index = []
pMax_index = []
SumTriplet(50000,pMin,p,pMax)
print(pMin)
print(p)
print(pMax)

for i in range(0,len(pMin)):
    if isprime(pMin[i]) == True:
        pMin_index.append(i)

for i in range(0,len(p)):
    if isprime(p[i]) == True:
        p_index.append(i)

for i in range(0,len(pMax)):
    if isprime(pMax[i]) == True:
        pMax_index.append(i)

for i in range(0,len(p)):
    neighCounter = 0
    # print("This is I: " + str(i))
    for k in range(0,len(pMin_index)-1):
        if i == pMin_index[k]:
            neighCounter += 1
        if i == pMin_index[k-1]:
            neighCounter += 1
        if i == pMin_index[k+1]:
            neighCounter += 1
    for k in range(0,len(pMax_index)-1):
        if i == pMax_index[k]:
            neighCounter += 1
        if i == pMax_index[k-1]:
            neighCounter += 1
        if i == pMax_index[k+1]:
            neighCounter += 1
    # if neighCounter >= 2:


print(pMin_index)
print(p_index)
print(pMax_index)
