import random


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.age}{self.name}"

    def main(x):
        x = []


class Person2():

    def __init__(self, name, age):
        self.name = name
        self. age = age

    def __str__(self):
        return f'{self.name}{self.age}'


class Employee(Person):

    def __init__(self, salary, commision):
        super().__init__(salary, commision)
        self.salary = ["bani"]
        self.commision = ["gros"]

    def commision_calculate(self):
        return f'{self.salary}'+'{self.commision}'

    def November(self):
        self.salary = 5000


class CV(Person):

    def __init__(self, companies, jobs):
        super().__init__(companies, jobs)
        self.companies = {
            "Banca Transilvania": "Ofiter Bancar",
            "DIGI": "Agent CallCenter",
            "Orange": "Operator Vanzari prin Telefon"
        }
        self.jobs = {

        }
        # print(self.companies)

    def myfunc(self):
        return f'{self.companies}'+'{self.jobs}'


class Future(Person):

    def __init__(self, preconization, x):
        super().__init__(preconization, x)
        self.preconization = 2022

    def myfunc1(self):
        return self.preconization

class Enemy(Person):

    def __init__(self, money, name):
        super().__init__(money, name)
        name = 'Iliescu Moldovan Anton Francisc'

    def myfunc(self):
        return f'{self.name}'

class Enemy_cash(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y)
        x = 200
        y = []

    def myfunc(self):
        return super().myfunc()
    

p1 = Person("Bogdan", 30)
# print(f'{p1.name} are {p1.age} ani')
p2 = Person2("Bebe", 30)
print(f'{p2.name} are {p2.age} ani')
p1.main()
# p2.main()
e1 = Employee("Bogdan", 5000)
e1.commision_calculate()
e1.November()
print(f'{p1.name} are {p1.age} ani si castiga {e1.salary} lei si comision {e1.commision}')
cv1 = CV("Bogdan", 30)
cv1.myfunc()
print(f'El a lucrat la {cv1.companies}')
x = Future("Bogdan", 30)
x.myfunc1()
print(
    f'Pana la finalul lui {x.preconization} se angajeaza in IT pe testare :D :D :D')
random.__dict__
y = Enemy('Iliescu Moldovan Anton Francisc', 30)
y.myfunc()
print(f'{y.name} dusmanul numarul unu a lui Bogdan')
z = Enemy_cash(200, 'Iliescu')
z.myfunc()
print(f'S-a imprumutat cu {z.myfunc()} lei, iar Anton s-a imbatat si a uitat sa plateasca :D :D :D')



def main():
    pass


if __name__ == '__main__':
    main()
