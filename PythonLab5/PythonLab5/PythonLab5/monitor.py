from datetime import datetime

class Monitor: 
    def __init__(self, brand, model, year, cost, data, surname, name):
        self.brand = brand
        self.model = model
        self.year = year
        self.cost = cost
        self.data = data
        self.surname = surname
        self.name = name

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}'\
            .format(self.brand, self.model, self.year, self.cost,
                self.data, self.surname, self.name) 