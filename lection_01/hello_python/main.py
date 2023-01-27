from Department import Department
from Worker import Worker
from DataBase import DataBase

dep1: Department = Department(0, "Информационный технологии")
dep2: Department = Department(1, "Отдел кадров")
dep3: Department = Department(2, "Бухгалтерия")

# print(dep1.get_info())
# print(dep2)
# print(dep3)

worker1: Worker = Worker(0, "Мария Ивановна", 23, 1234, 2)
worker2: Worker = Worker(1, "Марина Степановна", 26, 3456, 0)
worker3: Worker = Worker(2, "Мария Ивановна", 23, 1000, 2)
worker4: Worker = Worker(3, "Игнат Петрович", 33, 5432, 0)

db: DataBase = DataBase()

db.append_worker(worker1)
db.append_worker(worker2)
db.append_worker(worker3)
db.append_worker(worker4)

db.append_dep(dep1)
db.append_dep(dep2)
db.append_dep(dep3)

print(db.select_all_dep())
print("===========")
print(db.select_all_worker())

print(db.report())

print("done")