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
horse.get_descriptive()#须运行这个函数，不然得不到self.info，报错

horse.write_speed(10)
