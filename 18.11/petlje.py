pozicijaAutomobila = 0
pozicijaCilja = 10
# pozicijaAutomobila +=2
# print(pozicijaAutomobila == pozicijaCilja)

# pozicijaAutomobila +=2
# print(pozicijaAutomobila == pozicijaCilja)
# pozicijaAutomobila +=2
# print(pozicijaAutomobila == pozicijaCilja)
# pozicijaAutomobila +=2
# print(pozicijaAutomobila == pozicijaCilja)
# pozicijaAutomobila +=2
# print(pozicijaAutomobila == pozicijaCilja)

for ime in ["marko","milos","marija","sofija","ana"]:
    print("hello", ime)


print("prva sl. linija")

for broj in [1,2,3,4,5,6,7]:
    print("ovo je broj:",broj)



for broj in range (5,10, 2):
    print("stampanje broja:",broj)

for broj in range(100, 0, -1):
    print("prikaz:",broj)

for broj in range(-100,-200):
    print(broj)

pozicijaAutomobila = 0
pozicijaCilja = 10

for kretanje in range(5):
    pozicijaAutomobila += 2
    print(pozicijaAutomobila == pozicijaCilja)

startDate =2010
endDate = 2015

for allowed  in range(startDate,endDate):
    
    print("*",allowed,"*")
print()
# print("1\t2\t3\t")
# print("*********************")
# zeljenibroj = int(input("unesite broj:"))
# for brojac in range(1,zeljenibroj):
#     print(brojac*1, end="\t")
#     print(brojac*2,end="\t")
#     print(brojac*3,end="\n")

# for x in range(5):
#     for y in range(3):
#         print("ovo je x:",x,"ovo je y:",y)

# for taraba in range(6):
#     for zvezda in range(6):
#         if zvezda== taraba:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
    
        
    # print()


for taraba in range(6):
    for zvezda in range(6):
        if taraba == 0 or taraba == 5 or zvezda == 0 or zvezda == 5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
        
    print()





    


