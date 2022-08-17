satz = str(input("bitte Satz eingeben : "))
wortListe = satz.split(" ")

wortListe.reverse()
print(len(wortListe))
print(satz[::-1])
print(wortListe[1])