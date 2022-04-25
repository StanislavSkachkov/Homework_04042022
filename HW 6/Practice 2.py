class Road:
    _length = 5000
    _width = 20

    def m_road (self, m_asphalt=25, road_thickness = 5):
        result = self._length * self._width * m_asphalt * road_thickness / 1000
        print (f"При протяженности дороги {self._length} и ширине {self._width}, \n"
               f"а также массе асфальта {m_asphalt} и толщине {road_thickness} \n"
               f"масса асфальта составит {result} тонн")


road_1 = Road()
road_1.m_road()
