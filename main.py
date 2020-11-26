class garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]    
    def __repr__(self):
        return f"<Garage{self.cars}>"

    def __str__(self):
        return f'Garage with {len(self.cars)} cars'    
ford = garage()
ford.cars.append('fiesta')
ford.cars.append('focus')

print(ford.cars)

print(len(ford))

print((ford[0]))

for car in ford:
 print(car)

print(ford)