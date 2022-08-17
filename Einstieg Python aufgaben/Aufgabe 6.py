number1 = int(input("Bitte geben sie die 1. Zahl ein : "))
number2 = int(input("Nun bitte die 2. Zahl eingeben : "))
number3 = int(input("Nun bitte die 3. Zahl eingeben : "))

mittelwert = number1 + number2 + number3

mittelwert = mittelwert / 3

mittelwert = round(mittelwert, 5)

print("Der Mittelwert von", number1, number2, "und",  number3, "ist", mittelwert)