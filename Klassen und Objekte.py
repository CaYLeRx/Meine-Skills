
class Auto:
    def __init__(self):
        self.auto_marke = None
        self.power_score = None
        self.farbe = None


Auto1 = Auto()
print(Auto1.auto_marke)
Auto1.auto_marke = "Porsche"
Auto1.power_score = 460
Auto1.farbe = "Red"

print(Auto1.auto_marke)
print(Auto1.power_score)
print(Auto1.farbe)

Auto2 = Auto()

Auto2.auto_marke = "BMW"
Auto2.power_score = 210
Auto2.farbe = "Black"

print(Auto2.auto_marke)
print(Auto2.power_score)
print(Auto2.farbe)



