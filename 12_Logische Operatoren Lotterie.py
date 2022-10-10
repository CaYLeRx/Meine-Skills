print("Willkommen zur Lotterie!")
number1 = int(input("Bitte wähle eine Zahl von zwischen 1 und 49: "))
number2 = int(input("Bitte wähle eine Zahl von zwischen 1 und 49: "))
number3 = int(input("Bitte wähle eine Zahl von zwischen 1 und 49: "))
number4 = int(input("Bitte wähle eine Zahl von zwischen 1 und 49: "))

# Gewinnzahl 1: 5
# Gewinnzahl 2: 49
# Gewinnzahl 3: 37
# Gewinnzahl 4: 15

if number1 == 5:
    if number2 == 49:
        if number3 == 37:
            if number4 == 15:
                print("Herzlichen Glückwunsch Sie haben Gewonne!")
            else:
                print("Sie haben leider verloren ...")
        else:
            print("Sie haben leider verloren ...")
    else:
        print("Sie haben leider verloren ...")
else:
    print("Sie haben leider verloren ...")

# kurze Version!! 

print("Willkommen zur Lotterie!")
number1 = int(input("Bitte wähle eine Zahl von zwischen 1 und 49: "))
number2 = int(input("Bitte wähle eine Zahl von zwischen 1 und 49: "))
number3 = int(input("Bitte wähle eine Zahl von zwischen 1 und 49: "))
number4 = int(input("Bitte wähle eine Zahl von zwischen 1 und 49: "))

# Gewinnzahl 1: 5
# Gewinnzahl 2: 49
# Gewinnzahl 3: 37
# Gewinnzahl 4: 15

if number1 == 5 and number2 == 49 and number3 == 37 and number4 == 15:
    print("Herzlichen Glückwunsch Sie haben Gewonne!")
else:
    print("Sie haben leider verloren ...")
