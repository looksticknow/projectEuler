fibonacciNum = [1,2]
fibonacciSum = 0

for i in range(0,10000):
    sum_Temp = fibonacciNum[i]+fibonacciNum[i+1]
    if sum_Temp <= 4000000:
        fibonacciNum.append(fibonacciNum[i]+fibonacciNum[i+1])
    else:
        break

for i in range(0,len(fibonacciNum)):
    if fibonacciNum[i] % 2 == 0:
        fibonacciSum += fibonacciNum[i]
    else:
        pass

print(fibonacciSum)
