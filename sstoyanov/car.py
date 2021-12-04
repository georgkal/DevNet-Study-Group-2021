#define cas Car- define object Car
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    #define method object 
    def OrderCar(self):
        print ("Your car selection is: Model - {}, make -{}".format(self.model, self.make))

if __name__=="__main__":
    model = input("Please type model of your car: ")
    make = input("Please type make of your car: ") 
    my_car = Car(make, model) 
    my_car.OrderCar()
    print(my_car.model)