import random
from time import sleep

class Student:
    def __init__(self, n):
        self.name = n
        self.gladness = 0
        self.progress = 0
        self.money = 0
        #Студент представляется
        self.greeting()
    def greeting(self):
        print(f"I am {self.name}")
    def rest(self):
        #gladnes растет, progress уменьшается (1-3)
        self.gladness += random.randint(1, 3)
        self.progress -= random.randint(1, 3)
        self.money -= random.randint(1, 10)
        #выводим в консоль текущий уровень счастья и прогресса
        print(f"{self.name} | Rest | Gladness: {self.gladness} | Progress: {self.progress}")
    def study(self):
        #gladnes уменьшается, progress растет (1-3)
        self.gladness -= random.randint(1, 3)
        self.progress += random.randint(1, 3)
        self.money += random.randint(1, 10)
        # выводим в консоль текущий уровень счастья и прогресса
        print(f"{self.name} | Rest | Gladness: {self.gladness} | Progress: {self.progress}")
    def study(self):
        self.gladness += random.randint(1, 3)
        self.progress -= random.randint(1, 3)
        self.money += random.randint(1, 10)
        #выводим в консоль текущий уровень счастья и прогресса
        print(f"{self.name} | Study | Gladness: {self.gladness} | Progress: {self.progress}")
    def work(self):
        self.money += 7


students = []
students.append(Student("Maxim"))
students.append(Student("Kolya"))
students.append(Student("Andrey"))

gwinner = None
pwinner = None
day = 1
while True:
    print("Day:365 ", day)
    #цикл который проходит по всем студентам
    for student in students:
        actions = [student.rest, student.study, student.work]
        action = random.choice(actions)
        action()
        #проверяете если счастье студента больше или равно 100 и нет gwinner`а
        if student.gladness >= 100 and not gwinner:
            gwinner = student
        #проверяете если прогресс студента больше или равно 100 и нет pwinner`а
        if student.progress >= 100 and not pwinner:
            pwinner = student
         # проверяете если денги студента больше или равно 100 и нет pwinner`а
        if student.money >= 100 and not pwinner:
            pwinner = student

    day += 1
    #если есть gwinner and pwinner
    if gwinner and pwinner:
        break

print(gwinner.name + " первый достиг максимальный уровень счастья")
print(pwinner.name + " первый достиг максимальный уровень прогресс")
print(money.name + " первый достиг максимальный уровень денег")