palindrom = input("Wort eingeben, um zu testen, ob es ein Palindrom ist : ")
palindrom1 = palindrom.lower()
if palindrom1 == palindrom1[::-1]:
    print(palindrom, "ist ein Palindrom.")
else:
    print(palindrom, "ist kein Palindrom")