sekunde = 10

while sekunde > 0:
    print(sekunde)
    sekunde -= 1
import random
baterija = 90 
while baterija > 0:
    print("mozes koristiti telefon:",baterija,"%")
    baterija -= random.randint(5,20)
print("baterija je prazna")

for broj in range(11):
    if broj == 2:
        continue
    print(broj)

