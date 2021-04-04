class DataScientist:
    #defining a function
    def __init__(self, name, age, position, salary):
        #instance attributes that we will pass later inside the instance

        self.name = name
        self.age = age
        self.position = position
        self.salary = salary   

#outside the class
role = DataScientist("Sneha Roy", 24, "Senior", 45000)
print(role.name, "\n", role.age, "\n", role.position, "\n",role.salary)