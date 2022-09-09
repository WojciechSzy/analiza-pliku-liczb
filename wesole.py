dlugoscciagu = []
liczbywyjsciowe = []
iloscwesolych = 0
liczbywyjsciowedlamaxdl = []

# 4.1 Dla zakresu liczb od 1 do 1000 podaj liczby wesołe, dla których otrzymujemy największą liczbę liczb wesołych w
# cyklu obliczeniowym. W odpowiedzi w pierwszym wierszu wypisz największą liczbę liczb w takim cyklu, a w drugim
# wierszu wypisz wyjściowe liczby wesołe

# 4.2 Podaj, ile z podanych w pliku liczb to liczby wesołe

# 4.3 Podaj, ile wyrazów tworzy
# najdłuższy rosnący podciąg liczb wesołych. W odpowiedzi wypisz kolejno: długość, pierwszy
# i ostatni wyraz podciągu

# 4.4 Wesołe liczby pierwsze to liczby, które jednocześnie są wesołe i pierwsze. Podaj, ile z podanych
# w pliku liczb to takie liczby

def czywesola(liczba):
    dlugoscciagux = 0
    potegi = set()
    l = liczba
    while l!=1:
        suma = 0
        for i in str(l):
            suma += int(i)**2
        if suma in potegi:
            return False
        potegi.add(suma)
        dlugoscciagux += 1
        l = suma
    dlugoscciagu.append(dlugoscciagux)
    liczbywyjsciowe.append(liczba)
    return True

# rozwiązanie dla 4.1

for i in range (1,1001):
    czywesola(i)
maxdl = max(dlugoscciagu)
for i, j in enumerate(dlugoscciagu):
    if j==maxdl:
        liczbywyjsciowedlamaxdl.append(liczbywyjsciowe[i])

# rozwiązanie dla 4.2

f = open("liczby.txt")
for i in f:
    slowo = i.strip()
    if czywesola(slowo):
        iloscwesolych += 1

# rozwiązanie dla 4.3

f = open("liczby.txt")
# zapiszf = open("liczby_wesole.txt", 'a')
porownanie = []
for i in f:
    if czywesola(i.strip()):
        # zapiszf.write(i)
        porownanie.append(int(i.strip()))
f.close()
# zapiszf.close()

ile=1
ciagirosnace = []
for i in range(len(porownanie)-1):
    ciagirosnace.append(ile)
    if porownanie[i]<porownanie[i+1]:
        ile += 1
    else:
        ile = 1
ciagirosnace.append(ile)

def czypierwsza(x):
    for i in range (2, x//2+1):
        if x%i == 0:
            return False
    return True

wesolepierwsze = 0
for i in porownanie:
    if czypierwsza(i):
        wesolepierwsze += 1

print('4.1:')
print('największa długość ciągu:', maxdl)
print('wyjściowe liczby wesołe:', liczbywyjsciowedlamaxdl)
print('4.2:')
print('ilość liczb wesołych:', iloscwesolych)
print('4.3:')
print('Długość najdłuższego ciągu rosnącego:', max(ciagirosnace))
print(ciagirosnace.index(max(ciagirosnace)))
print(porownanie[ciagirosnace.index(max(ciagirosnace))])
print(porownanie[ciagirosnace.index(max(ciagirosnace))-max(ciagirosnace)+1])
print('4.4:')
print('Liczby wesołe pierwsze:', wesolepierwsze)
