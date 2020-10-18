from Person import Person
from datetime import date
import fnmatch


class Doctor(Person):
    def __init__(self, surname, name, fname, birth, specialty, salary, patient_count):
        self.specialty = specialty
        self.salary = salary
        self.patient_count = patient_count

    def getSpecialty(self):
        return self.specialty

    def countPatient(self, lastCount):
        return lastCount + self.patient_count