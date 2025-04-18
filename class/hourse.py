class Horse():
    def __init__(self,age,category,gender):
        self.age=age
        self.category=category
        self.gender=gender
        self.new_speed=0
    def get_descriptive(self):
        self.info='一匹'+self.category+str(self.age)+'岁的'+self.gender+'马'
    def write_speed(self,new_speed):
        self.new_speed=new_speed
        addr="在草原上奔跑的速度为："
        print(self.info+addr+str(self.new_speed)+"km/h.")

horse=Horse(12,'阿拉伯','公')
horse.get_descriptive()#得先运行这个函数，才得到self.info，不然会报错
horse.write_speed(10)


class Camel(Horse):
    def __init__(self,age,category,gender):

        super().__init__(age,category,gender)#super().__init__(没有self,age,category,gender)，否则会报错


    def write_speed(self,new_speed):
        self.new_speed=new_speed
        addr="在沙漠上奔跑的速度为："
        print(self.info.replace('马','骆驼')+addr+str(self.new_speed)+"km/h.")

camel=Camel(12,"双峰",'公')
camel.get_descriptive()
camel.write_speed(10)

