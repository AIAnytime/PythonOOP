#child class can has its own attributes and methods 
#we can extend few attributes of parent class using super keyword

#parent class
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working......")

#first child class
class DataScientist(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level
    
    #own function
    def data_pipeline(self):
        print(f"{self.name} is building the data pipeline...")

#second child class
class MLEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level
    
    #own function
    def deployment(self):
        print(f"{self.name} is deploying the model....")
        

#create the instances
ds = DataScientist("Sonu", 24, 50000, "Senior")
ml = MLEngineer("Sneha", 23, 40000, "Junior")

print(ds.level)
print(ml.level)
ds.data_pipeline()
ml.deployment()