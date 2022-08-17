print("Hallo")
print("Bitte beantworte diese Fragen richtig, denn deine Fehlversuche werden gezählt.")
i = "ja"
while not i == "nein":
    answer1 = int(input("Aus wie vielen Zahlen besteht das Binärsystem? "))
    x = 0
    a = True
    b = True
    c = True
    d = True
    e = True
    while a:
        if answer1 == 2:
            a = False
        elif answer1 == 1:
            print("Nein ganz sicher NICHT!!!")
            answer1 = int(input("Versuche es nochmals : "))
            x = x + 1
        else:
            answer1 = int(input("Versuche es nochmals : "))
            x = x + 1
    print("Bravo!")
    print("---------------------------------------")
    print("Kommen wir jetzt zur nächsten Frage")
    answer2 = input("Wer hat Tesla berühmt gemacht? ")
    while b:
        if answer2 == "Elon Musk":
            b = False
        elif answer2 == "Ich":
            answer2 = input("(-_-) Schön ware es. Bitte versuche es nochmal : ")
            x = x + 1
        else:
            answer2 = input("Versuche es nochmals : ")
            x = x + 1
    print("Bravo! Du kennst dich ja richtig aus.")
    print("---------------------------------------")
    print("Kommen wir zur nächsten Frage")
    answer3 = input("Wie heisst ein sehr Bekanntes spiel, welches mit Java programmiert wurde? ")
    while c:
        if answer3 == "Minecraft":
            c = False
        elif answer3 == "MC":
            c = False
        else:
            answer3 = input("Versuche es nochmals : ")
            x = x + 1
    print("Bravo! Wieder etwas richtig")
    print("---------------------------------------")
    print("Kommen wir zur nächsten Frage")
    answer4 = input("Welches ist die Haupstadt von der Schweiz? ")
    while d:
        if answer4 == "Bern":
            d = False
        elif answer4 == "Zürich":
            answer4 = input("NEIN!!! VERSUCHE ES NOCHMAL : ")
            x = x + 1
        else:
            answer4 = input("Versuche es nochmals : ")
            x = x + 1
    print("Bravo!")
    print("---------------------------------------")
    print("Kommen wir zur nächsten Frage")
    answer5 = input("Welcher PC-Kommponen ist das Herzstüch des PC's? ")
    while e:
        if answer5 == "CPU" or answer5 == "Prozessor":
            e = False
        elif answer5 == "Mainboard":
            answer5 = input("Das Mainbouard ist nicht das Herzstück. Probiere es erneut : ")
            x = x + 1
        else:
            answer5 = input("Versuche es nochmals : ")
            x = x + 1
    if x == 0:
        print("Bravo!")
        print("Du hast das Quiz erfolgreich ohne Fehler abgeschlossen")
    elif 0 < x < 4:
        print("Bravo! Schon wieder die richtige Antwort gefunden")
        print("Du hast das Quiz erfolgreich mit nur", x, "Fehler abgeschlossen")
    elif 3 < x < 6:
        print("Bravo!")
        print("Du hast das Quiz erfolgreich mit", x, "Fehler abgeschlossen")
    else:
        print("Bravo!")
        print("Du hast das Quiz NICHT erfolgreich abgeschlossen. Du hattest", x, "Fehler.")
    print("möchtest du das Quiz noch mal machen?")
    i = input("Bitte mit (ja) oder (nein) antworten : ")
print("Vielen Dank fürs spielen<3")