osoba = ["sofija ",20,"plava", True]
print(osoba)

print(osoba[0])
print("Godine", osoba[1])

automobili=["opel","mercedes","bmw"]

print(automobili[1])

#range
for x in range(10):
    print(x)

for x in range(1,10,2):
    print(x)

#string
    #  0123456789...
kurs = "python"


for x in range(len(osoba)):
    print("na poziciji",x,kurs[x])
    
ustanova = "IT Academy"
for indeks in range(len(ustanova)):
    print(ustanova[indeks])

primer = "zadatak1"
for indeks in range(len(primer)):
    print(primer[indeks])

brojKaraktera = len(primer)
indeks= 0
while indeks < brojKaraktera:
    print(primer[indeks])
    indeks+= 1

korisnickoime = "admin"
unetoKorIme = input("unesi korisnicko ime:")
if korisnickoime == unetoKorIme.lower():
    print("Dobrodosli")
else:
    print("pogresni podaci")

racunar = "laptop"
racunar