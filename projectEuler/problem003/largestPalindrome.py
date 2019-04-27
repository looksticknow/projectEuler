tall_Liste = []

for i in range(10,100):
    for k in range(10,100):
        tall_Liste.append(k*i)

def findPalindrome(tall):
    palinDrome_List = []
    tall_Temp = []
    counter = 0
    tall = str(tall)
    for i in range(0,len(tall)):
        tall_Temp.append(tall[i])

    if len(tall_Temp) % 2 == 0:
        print("WERE IN")
        tall_Lengde = int(len(tall_Temp)/2)
        for i in range(0,tall_Lengde):
            print(tall_Temp[i],tall_Temp[-i-i*1])
            if tall_Temp[i] == tall_Temp[-i-i*1]:
                counter += 1
                print(counter)
        if counter == tall_Lengde:
            palinDrome_List.append(tall)
    else:
        pass
    return palinDrome_List



for i in range(0,len(tall_Liste)):
    if findPalindrome(tall_Liste[i]) == []:
        pass
    else:
        print(findPalindrome(tall_Liste[i]))

print(findPalindrome(9009))
