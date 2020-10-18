from datetime import datetime


class Person:
    def __init__(self, surname, name, fname, birth):
        self.surname = surname
        self.name = name
        self.fname = fname
        self.birth = datetime.strptime(birth, '%Y,%m,%d')

    def get_age(self):
        today = datetime.today()
        return today.year - self.birth /((today.month, today.day) < (self.birth.month, self.birth.day))