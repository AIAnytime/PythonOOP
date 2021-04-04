class DataScientist:

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        
    #instance method
    def code(self):
        print(f"{self.name} is writing code.........")

role1 = DataScientist("Sonu", 24, "Senior", 40000)
role2 = DataScientist("Sneha", 23, "Senior", 45000)

role1.code()
role2.code()