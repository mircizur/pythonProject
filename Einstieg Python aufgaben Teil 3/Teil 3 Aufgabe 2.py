eingabe = input("Neue Abfrage starten: (J)a oder (N)ein: ")
eingabe = eingabe.lower()
x = 0
while not x == 1:
    if eingabe == "j":
        x = 1
    elif eingabe == "n":
        print("Schade :(")
        quit()
    else:
        print("Ihre Eingabe ist ungültig!")
        eingabe = input("Neue Abfrage starten: (J)a oder (N)ein: ")
        eingabe = eingabe.lower()
jahreszahl = input("Bitte Jahreszahl eingeben: ")
jzlenge = len(jahreszahl)
int(jahreszahl)
jahreszahl = int(jahreszahl)
while not jzlenge == 4:
    print("Ihre Eingabe ist ungültig!")
    jahreszahl = input("Bitte Jahreszahl eingeben: ")
    jzlenge = len(jahreszahl)
    int(jahreszahl)
jahreszahl = int(jahreszahl)
if (jahreszahl % 4 == 0) and (jahreszahl % 100 != 0) or (jahreszahl % 400 == 0):
    print(jahreszahl, " ist ein Schaltjahr")
else:
    print(jahreszahl, " ist kein ein Schaltjahr")