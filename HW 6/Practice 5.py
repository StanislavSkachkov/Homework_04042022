class Stationery:
    def __init__(self,title):
        self.title = title

    def draw_func(self):
        print ("Запуск отрисовки")


class Pen(Stationery):
    def draw_func(self):
        print ("Рисунок карандаша")


class Pencil(Stationery):
    def draw_func(self):
        print ("Запись ручки")


class Handle(Stationery):
    def draw_func(self):
        print ("Выделение маркером")



pen = Pen ('Ручка')
pencil = Pencil ('Карандаш')
handle = Handle ('Маркер')

print(pen.draw_func())
print(pencil.draw_func())
print (handle.draw_func())
