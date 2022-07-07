class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color, engine):
        pass
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color
        self.engine = engine

    def start_engine(self):
            print(f"Engine on {self.title} {self.model} started!")

    def stop_engine(self):
            print(f"Engine on {self.title} {self.model} stoped")

    def info(self):
        print(f'All info:{Bmw.title} {Bmw.model} {Bmw.weight} {Bmw.hp} {Bmw.nm} {Bmw.max_speed} {Bmw.color}\n')

Bmw = Car('Bmw', 'x6', 2300, 400, 700, 250, 'black', '4wd')
Bmw.start_engine()
print(Bmw.title, Bmw.model, Bmw.weight, Bmw.hp, Bmw.nm, Bmw.max_speed, Bmw.color, Bmw.engine)

