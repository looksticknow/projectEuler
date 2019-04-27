triNum_List = []
divisor_List = []
triNum = 10+1

for i in range(0,triNum-1):
    divisor_List.append([])

# Making the list of the triangular numbers up to n
for i in range(1,triNum+1):
    sum = 0
    for k in range(0,i):
        sum += k
    if sum == 0:
        pass
    else:
        triNum_List.append(sum)

print(triNum_List)
print(divisor_List)

for i in range(0,len(divisor_List)):
    for k in range(1,triNum_List[i]+1):
        if triNum_List[i] % k == 0:
            divisor_List[i].append(k)

# Finding the first triangle number to have over five hundred divisors!
biggestDiv = len(divisor_List[0])
i_count = 0
for i in range(1,len(divisor_List)):
    if len(divisor_List[i]) > biggestDiv:
        biggestDiv = len(divisor_List[i])
        i_count = i
        if biggestDiv >= 500:
            break
print(biggestDiv)
print("With index of: " + str(i_count))
print("With the triangle number of: " + str(divisor_List[i][-1]))
