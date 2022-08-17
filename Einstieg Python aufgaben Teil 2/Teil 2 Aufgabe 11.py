var1 = int(input("Was gibt 101 + 10 = "))
misstakes = 0
while not var1 == 111:
        misstakes = misstakes + 1
        var1 = int(input("Nochmal. Was gibt 101 + 10 = "))
print("Richtig")
print("du hattest",misstakes, "Fehlversuche")