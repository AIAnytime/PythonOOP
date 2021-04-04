#we can override the function of parent class
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working!!")

#child class
class DataScientist(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    #override the function from parent class
    def work(self):
        print(f"{self.name} is working on the data science pipeline......")

#second child class
class MLEngineer(Employee):
    def __init__(self, name, age, salary, level, leave):
        super().__init__(name, age, salary)
        self.level = level
        self.leave = leave
        
    #override the function
    def work(self):
        print(f"{self.name} is working on ML Models......")

#create the instances
ds = DataScientist("Sonu", 24, 50000, "Senior")
ml = MLEngineer("Sneha", 23, 40000, "Junior", 20)

print(" Name is: ", ds.name, "\n", "Age: ", ds.age, "\n", "Salary: ",ds.salary, "\n", "Level:", ds.level)
ds.work()
ml.work()