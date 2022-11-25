osoba = ["sofija",25,False]
for x in range(len(osoba)):
    print(osoba[x])

for osobina in osoba:
    print(osobina)

voceIPovrce= ["jabuka","mandarina","luk","lubenica","banana","limun","krastavac"]
for stavka in voceIPovrce:
    print(stavka)

for i in range(len(voceIPovrce)):
    print(i ,voceIPovrce[i])

for indeks , vrednost in enumerate(voceIPovrce):
    print(indeks,vrednost)

automobili = ["citroen","kia","yugo","renault"]

for indeks,vrednost in enumerate(automobili):
    print("Pozicija:",indeks,"auto:",vrednost)


automobili.append("Mercedes")
automobili[2]= "opel corsa"
print(automobili)
automobili[3]= "kia sportage"
del automobili[2]
print(automobili)

automobili.remove("citroen")
print(automobili)
automobili.pop(0)
print(automobili)
automobili.clear()
print(automobili)

automobili = ["citroen","kia","yugo","renault","audi"]
automobiliAkcija = []
for i in range(len(automobili)):
    if i== 1 or i ==2 or i==3:
        automobiliAkcija.append(automobili[i])

print(automobiliAkcija)

automobiliAkcija = automobili[1:4]
print(automobiliAkcija)

a = [1,2,3,4,5,6,7,8,9]

paran = []
neparan =[]
for brojevi in a:
    if brojevi % 2==0:
        paran.append(brojevi)
    else:
        neparan.append(brojevi)

print(paran)
print(neparan)

        