class Vehicle: # Это класс "автомобиль"
    def __init__(self, consump, distance, volume):
        self.consump = consump   #свойство расход бензина на 100 км
        self.distance = distance  #пройденный маршрут, км 
        self.volume = volume  #скорость 
    def get_consump(self):   # Метод для вывода свойства в print
        return self.consump
    def get_distance(self):   # Метод для вывода свойства в print
        return self.distance 
    def get_volume(self):   # Метод для вывода свойства в print
        return self.volume
    # Метод расчета топлива, необходимого, чтобы проехать расстояние.
    def getPetrol(self):
        return self.consump * (self.distance/100)
Suzuki = Vehicle(9, 800, 100)   
Volvo = Vehicle(15, 800, 90)
print('Расход топлива для Сузуки =', Suzuki.getPetrol())     
print('Расход топлива для Вольво =', Volvo.getPetrol())

class Truck(Vehicle): #Это дочерний класс "грузовой автомобиль"
    time = 0 #время для доставки груза"
    def __init__(self, consump, distance, volume):
        Vehicle.__init__(self, consump, distance, volume)
        self.time = distance / volume
    def get_time(self):
        return self.time
Man_truck = Truck(15, 800, 90)
print('Время доставки грузовиком MAN =', Man_truck.get_time())

 