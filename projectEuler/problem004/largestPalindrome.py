tall_Liste = []
palinDrome_List = []
tall_REKKE = []

for i in range(100,1000):
    for k in range(100,1000):
        tall_Liste.append(k*i)
print(tall_Liste)

def findPalindrome(tall):
    tall_Temp = []
    counter = 0
    tall = str(tall)
    for i in range(0,len(tall)):
        tall_Temp.append(tall[i])

    if len(tall_Temp) == 2:
        if tall_Temp[0] == tall_Temp[1]:
            palinDrome_List.append(int(tall))
    elif len(tall_Temp) == 1:
        palinDrome_List.append(int(tall))
    elif len(tall_Temp) % 2 == 0:
        tall_Lengde = int(len(tall_Temp)/2)
        for i in range(0,tall_Lengde):
            if tall_Temp[i] == tall_Temp[-i-1]:
                counter += 1
        if counter == tall_Lengde:
            palinDrome_List.append(int(tall))
    elif len(tall_Temp) % 2 != 0:
        tall_Lengde = int(len(tall_Temp)) - 1
        if tall_Lengde % 2 == 0:
            tall_Lengde = int(len(tall_Temp)/2)
            for i in range(0,tall_Lengde):
                if tall_Temp[i] == tall_Temp[-i-1]:
                    counter += 1
    else:
        pass

for i in range(0,len(tall_Liste)):
    if findPalindrome(tall_Liste[i]) == None:
        pass
    else:
        palinDrome_List.append(findPalindrome(tall_Liste[i]))

biggestNumber = palinDrome_List[0]
for i in range(0,len(palinDrome_List)):
    if palinDrome_List[i] > biggestNumber:
        biggestNumber = palinDrome_List[i]

print(biggestNumber)
