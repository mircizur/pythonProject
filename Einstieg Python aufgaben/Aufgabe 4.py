print("Bitte in ganze Zahlen angeben.")
name = input("Deinen Namen bitte : ")
weight = float(input("Dein Gewicht bitte : "))
size = float(input("Deie Grösse bitte : "))

bmi = round(weight / size ** 2, 1)

print(name, ", dein BMI ist", bmi)