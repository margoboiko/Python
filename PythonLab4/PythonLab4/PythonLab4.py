from datetime import date

from Doctor import Doctor

def doctor():
    surname = input('surname: ')
    name = input('name: ')
    fname = input('father name: ')
    birth = input('birth (enter year-month-day): ')
    specialty = input('specialty: ')
    salary = int(input('salary: '))
    patient_count = int(input('patient count: '))
    return Doctor(surname, name, fname, birth, specialty, salary, patient_count)

n = int(input('n = '))

doctors = [doctor() for i in range(n)]
print(doctors)
specialty = input('enter specialty: ')

countPatient = 0
AverageSalary = 0
salaryArray = []

for j in range(len(doctors)):
    if doctors[j].getSpecialty() == specialty:
        countPatient = doctors[j].countPatient(countPatient)
        salaryArray.append(doctors[j].salary)

AverageSalary = sum(salaryArray)/len(salaryArray)
print("All patient count = " , countPatient)
print("Average salary = ",AverageSalary)