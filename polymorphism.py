class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def work(self):
        print(f"{self.name} is working...........")

class DataScientist(Employee):
    def __init__(self, name, age, salary, level, role):
        super().__init__(name, age, salary)
        self.level = level
        self.role = role
        
    def work(self):
        print(f"{self.name} is building data pipeline....")
    
class MLEngineer(Employee):
    def __init__(self, name, age, salary, level, leave):
        super().__init__(name, age, salary)
        self.level = level
        self.leave = leave
        
    def work(self):
        print(f"{self.name} is creating models........")

ds = DataScientist("Sonu", 24, 50000, "Senior", "End to End Pipeline")
ml = MLEngineer("Sneha", 23, 45000, "Junior", 25)

#concept of polymorphism
list_of_emp = [DataScientist("Sonu", 24, 50000, "Senior", "End to End Pipeline"),
MLEngineer("Sneha", 23, 45000, "Junior", 25)]

def motivate_emp(list_of_emp):
    for employee in list_of_emp:
        employee.work()

motivate_emp(list_of_emp)
