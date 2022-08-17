import webbrowser  # Quelle:https://www.python-lernen.de/webbrowser-mit-python-nutzen.htm
kategorien = {
    "katGamingFragen": {1: "Wann wurde das Erste Videospiel programmiert?",
                  2: "Welches ist das meisste verkaufte Spiel der Welt?",
                  3: "In welchem Jahr ist die erste Playstation 1 rausgekommen",
                  4: "Was Bedeutet GG?",
                  5: "Wie heisst das erste Videospiel"},
    "katGamingAntworten": {1: "1958",
                  2: "Minecraft",
                  3: "1994",
                  4: "Good Game",
                  5: "Tennis for Two"},
    "katMusik": {1: "Von wem ist (Symphony No. 9)? Bitte ganzer Name.", 2: "Ludwig van Beethofen",
                 3: "Wie heisst der bekannteste Song von Lied von Los del Río?", 4: "Macarena",
                 5: "Von wem ist der Song Thriller?", 6: "Michael Jackson",
                 7: "Woher kommt der Musikstil Reggae", 8: "Jamaika",
                 9: "Wie nennt man das Textbuch für eine Oper, eine Operette oder ein Ballett?", 10: "Libretto",
                 11: "Wie heissen die bis zu 4 m langen Holztrompeten, die in der Alpenregion beheimatet sind?", 12: "Alphorn",
                 13: "Wie viele noten hat eine tonleiter", 14: "8",
                 15: "Von wem ist das Lied Venom?", 16: "Eminem",
                 17: "Wie viele Saiten hat eine Gitarre meistens?", 18: "6",
                 19: "Mache weiter: Never gonna give you up...", 20: "Never gonna let you down"},
    "katMusik": {1: "Von wem ist (Symphony No. 9)? Bitte ganzer Name.", 2: "Ludwig van Beethofen",
                 3: "Wie heisst der bekannteste Song von Lied von Los del Río?", 4: "Macarena",
                 5: "Von wem ist der Song Thriller?", 6: "Michael Jackson",
                 7: "Woher kommt der Musikstil Reggae", 8: "Jamaika",
                 9: "Wie nennt man das Textbuch für eine Oper, eine Operette oder ein Ballett?", 10: "Libretto",
                 11: "Wie heissen die bis zu 4 m langen Holztrompeten, die in der Alpenregion beheimatet sind?", 12: "Alphorn",
                 13: "Wie viele noten hat eine tonleiter", 14: "8",
                 15: "Von wem ist das Lied Venom?", 16: "Eminem",
                 17: "Wie viele Saiten hat eine Gitarre meistens?", 18: "6",
                 19: "Mache weiter: Never gonna give you up...", 20: "Never gonna let you down"},
    "katWitze": {1: ""},
    "katSchweiz": {1: "Wie viele Einwohner hat die Schweiz?\nZahl ganz ausgeschrieben z.B. 1,000,000\nund auf den "
                      "Hunderttausender gerundet", 2: "8,600,000",
                   3: "Welche Sprache wird in der Schweiz am meissten gesprochen?", 4: "Deutsch",
                   5: "wie heisst die Sprachgrenze der Schweiz?", 6: "Röstigraben",
                   7: "In welchem Jahr wurde die Schweiz gegründet", 8: "1848",
                   9: "Wie viele Kantone hat die Schweiz?", 10: "26"
                   },
    "katAutos": {}
}

print("Hallo, dies ist ein Quiz mit verschiedenen Kategorien.")
print("Wollen Sie das Quiz starten? Bitte geben sie (J) für ja ein oder (N) für nein.")
spielstart = input()
spielstartLower = spielstart.lower()

while spielstartLower != "j" and spielstartLower != "n":
    spielstart = input("Ihre eingabe ist ungültig, bitte erneut eingeben")
    spielstartLower = spielstart.lower()
if spielstartLower == "n":
    print("Schade :(")
    quit()
else:
    print("Nun kommen wir zu den Kategorien")
print("Ihnen stehen 5 Kategorien zur verfügung")

for x in range(1, 11, 2):
    print(kategorien["katSchweiz"][x])
    print(kategorien["katSchweiz"][x + 1])
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
webbrowser.open(url)
