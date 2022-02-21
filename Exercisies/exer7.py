from math import sqrt

class Car:
    def init(self):
        self.fuel = 100.0
        self.position = [0, 0]
    
    def print_info(self):
        print(self.fuel, self.position)
    
    def move(self, goal):
        distance = sqrt((self.position[0] - goal[0])**2 + (self.position[1] - goal[1])**2)
        print(distance)
        
        if self.fuel >= distance:
            print("移動しました")
            self.fuel -= distance
            self.position = goal.copy()
            print(f"残りの燃料:{self.fuel}")
        else:
            print("燃料が足りないので移動できません")
        
    def charge(self):
        self.fuel += 100 - self.fuel
        print(f"チャージしました:残り{self.fuel}")

car = Car()
car.init()
car.print_info()

x, y = (int(i) for i in input("x,y座標をスペース区切りで入力:").split())
car.move([x, y])
car.charge()