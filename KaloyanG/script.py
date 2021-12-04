
#Defeine class Car- define object Car
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    #Define method for object car
    def OrderCar(self):
        print("Your car selection is: Model - {}, Make -{}".format(self.model, self.make))

if __name__=="__main__":
    model = input("Please type model of your car: ")
    make = input("Please type make of your car: ")
    my_car = Car(make, model)
    my_car.OrderCar()
    print(my_car.model)
    my_car1 = Car(make, model)
    print(my_car1.model)