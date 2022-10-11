
class Auto:
    def __init__(self):
        self.auto_marke = None
        self.power_score = None
        self.farbe = None
   
    def drive(self, x, y):
        self.x_position += x
        self.y_position -= y


Auto1 = Auto()  #Auto Objekt 1
print(Auto1.x_position)
print(Auto1.y_position)
Auto1.drive(5, 2)
print(Auto1.x_position)
print(Auto1.y_position)


        
print(Auto1.auto_marke)
print(Auto1.power_score)
print(Auto1.farbe)


Auto2 = Auto() #Auto Objekt 2
print(Auto2.auto_marke)
Auto2.auto_marke = "BMW"
Auto2.power_score = 210
Auto2.farbe = "Black"

Auto3 = Auto1 #das Objekt greift auf das selbe Element zu

print(Auto1)
print(Auto2)
print(Auto3)
print(Auto1.power_score) 
print(Auto3.power_score) #referenz bleibt gleich
