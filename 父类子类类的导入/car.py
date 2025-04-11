class Car:
    def __init__(self,name):
        self.name=name
        self.mile=0

    def read_mile(self):
        mi=f"{self.mile}"
        return mi
    #没有return时，函数返回None.
    def mod_mile(self,num):
        self.mile=num

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size

    def describe_battery(self):#有self做参数
        print(f"{self.battery_size}")



class ElectricCar(Car):
    def __init__(self,name):
        super().__init__(name)#参数中没有self
        #super()特殊函数，能调用父类方法
        self.battery=Battery()
        #实例：Battery()没有参数，属性：battery






my_tesla=ElectricCar("keyan")
print(my_tesla.read_mile())
my_tesla.battery.describe_battery()
my_car=Car("gg")
print(my_car.mile)


'''
导入类car.py中有类Car,创建另一文件my_car.py,在my_car.py中导入类：
1  from car import Car
2  from car import Car,ElectricCar
3  import car
4  from car import *
5  from car import ElecctricCar as EC
'''
