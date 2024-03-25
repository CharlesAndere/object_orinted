class Tribe:
    name = ""
    age = 0
    gender = ""
    tribe = ""

    def __init__(self,name, age, gender, tribe):
        self.name = name
        self.age = age
        self.gender = gender
        self.tribe = tribe

    def displayThis(self):
        print("My name is:", self.name, " age:", self.age, "gender:", self.gender, "and my tribe is:", self.tribe)

    def speaks(self):
        print("I speak Luhya")

class Kikuyu(Tribe):
        def speaks(self):
            print("I speak Kikuyu")

class Luo(Tribe):
        def speaks(self):
            print("I speak Luo")

class Kamba(Tribe):
        def speaks(self):
             print("I speak Kamba")

tir = Tribe("Charles Ander", 20, "male", "Luyha")
tir.displayThis()
tir.speaks()

tir1 = Kikuyu("Mark Kamau", 18, "male", "Kikuyu")
tir1.displayThis()
tir1.speaks()

tir2 = Luo("Davis onyango", 8, "male", "Luo")
tir2.displayThis()
tir2.speaks()

tir3 = Kamba("Jack Kisungu", 14, "male", "Kamba")
tir3.displayThis()
tir3.speaks()
