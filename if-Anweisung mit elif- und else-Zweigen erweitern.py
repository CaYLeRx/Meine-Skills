age = int(input("Bitte gebe dein Alter an: "))

if age < 21:
    print("Achtung der Nutzer ist jünger als 21")
    print("Zugang 'GESPERRT' ")
elif age == 21:
    print("Der Nutzer ist exakt 21")
    print("Willkommen")
else:
    print("Der Nutzer ist volljährig")
    print("Willkommen")

print("ENDE")
