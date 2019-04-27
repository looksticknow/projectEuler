from sympy import primerange

def countSum(list):
    sum = 0
    for i in range(0,len(list)):
        sum += list[i]
    return sum


primeNumber_List = []
primeStart = 1
primeStop = 2000000

for i in primerange(primeStart,primeStop):
    primeNumber_List.append(i)

print(primeNumber_List)
print(countSum(primeNumber_List))
