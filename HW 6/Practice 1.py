import time


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]


    def running(self):
        m = 0
        while m != "Q":
            print (f'Светофор работает. {TrafficLight.__color[0]}')
            time.sleep(7)
            print(f'Светофор переключился. {TrafficLight.__color[1]}')
            time.sleep(2)
            print(f'Светофор переключился. {TrafficLight.__color[2]}')
            time.sleep(8)
            m = input ("Для запуска светофора еще раз введите любой символ, для остановки введите Q ")


traffic_light_1 = TrafficLight()
traffic_light_1.running()
