for x in range(6):
    for y in range(6):
        if y>x:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()

auto = 0
cilj = 100
brzina = 10
gorivo = 11
while auto<cilj:
    print("voznja u toku")
    auto += brzina
    gorivo-= 5
    if gorivo == 0:
        print("nema goriva")
        break

else:
    print("end")

