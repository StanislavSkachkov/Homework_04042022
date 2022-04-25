class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print ("Поехали")


    def car_stop(self):
        print ("Остановка")


    def car_turn_right (self):
        print ("Поворот направо")


    def car_turn_left(self):
        print("Поворот налево")


    def show_speed(self, speed):
        print (f'Текущая скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 60:
            print (f'Вы превысили ограничение по скорости. Текущая скорость {speed}')
        else:
            print (f'вы едите с разрешенной скоростью {speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 40:
            print (f'Вы превысили ограничение по скорости. Текущая скорость {speed}')
        else:
            print (f'вы едите с разрешенной скоростью {speed}')


class SportCar(Car):
    '''спорт машина'''


class PoliceCar(Car):
    '''полицейская машина'''


bmw = TownCar(80, "Red", "BMW", False)
porsche = SportCar(140, "Orange", "Porsche", False)
kamaz = WorkCar (50 , "Yellow", "Kamaz", False)
police_car = (150 , "Black", "Police", True)

print (porsche.car_turn_right())
print (porsche.show_speed(0))
