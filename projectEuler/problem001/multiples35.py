sumList = []

for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            sumList.append(i)

print(sumList)
sum = 0
for i in range(0,len(sumList)):
    sum += sumList[i]
print(sum)
