done = False
triNum_Start = 0
triNum_Stop = 1000
stepSize = int(triNum_Stop/10)
triNum_Stop += 1

while not done:
    triNum_List = []
    divisor_List = []

    for i in range(0,int((triNum_Stop-1)/stepSize)):
        divisor_List.append([])

    # Making the list of the triangular numbers up to n

    for i in range(0,triNum_Stop+1,stepSize):
        sum = 0
        for k in range(0,i):
            sum += k
        if sum == 0:
            pass
        else:
            triNum_List.append(sum)

    for i in range(0,len(divisor_List)):
        for k in range(1,triNum_List[i]+1):
            if triNum_List[i] % k == 0:
                divisor_List[i].append(k)

    biggestDiv = len(divisor_List[0])
    for i in range(1,len(divisor_List)):
        if len(divisor_List[i]) > biggestDiv:
            biggestDiv = len(divisor_List[i])
            if biggestDiv >= 500:
                done = True

    print(divisor_List)
    if biggestDiv < 500:
        print("Trinum stop pre: " + str(triNum_Stop))
        triNum_Stop += 1000
        print("Trinum stop post: " + str(triNum_Stop))
        print("Trinum start pre: " + str(triNum_Start))
        triNum_Start += 1000
        print("Trinum start post: " + str(triNum_Start))

print(divisor_List)
