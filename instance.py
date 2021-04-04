class AIEngineer:

    #define a class attributes
    added_advantage = "Deployment"

    def __init__(self, name, age, salary, level):
        #instance attributes
        self.name = name;
        self.age= age;
        self.salary = salary;
        self.level = level;

role = AIEngineer("Sonu", 24, 40000, "Senior")
print( role.name, "\n", role.age, "\n", role.salary, "\n", role.level ,"\n")
print("His added advantage is:", role.added_advantage)
#print(AIEngineer.name), will throw an error as instance attributes are only 
#accesible by instance not by class datastructure