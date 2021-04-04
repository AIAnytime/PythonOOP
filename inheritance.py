#Base or parent class
class Employee():
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def work(self):
        print(f"{self.name} is working..........")

#child class that will inherit the attributes and methods from parent class
class DataScientist(Employee):
    pass

class MachineLearningEngineer(Employee):
    pass

#create the instances 

ds = DataScientist("Sonu", 24, "Senior Data Scientist", 50000)
ml = MachineLearningEngineer("Sneha", 23, "Junior ML Engineer", 40000)

print(ds.name, ds.age, ds.level, ds.salary)
ds.work()

print(ml.name, ml.age, ml.level, ml.salary)
ml.work()