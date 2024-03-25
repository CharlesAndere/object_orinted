class Car:
    model = ""
    speed = 0
    nick_name = ""
    def __init__(self, model, speed, nick_name):
        self.model = model
        self.speed = speed
        self.nick_name = nick_name

    def driving(self):
        print("the", self.model, "driver is driving")

    def stop(self):
        print("the", self.model, "driver is stopping")
car1 = Car("BMW", "100km/p", "be my wife")
print(car1.model)
print(car1.speed)
print(car1.nick_name)
car1.driving()
car1.stop()

car2 = Car("toyota", "130km/p", "old")
print(car2.model)
print(car2.speed)
print(car2.nick_name)
car2.driving()
car2.stop()
