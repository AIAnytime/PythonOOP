#create a class
class Political_Party:

    #init
    def __init__(self, name, age, designation, salary):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary

    #first instance method
    def home_state(self, state):
        print(f"{self.name} is from {state}.....")
    
    #second instance method
    def party(self, partyname):
        print(f"{self.name} belongs to {partyname}.....")

    #create an information method
    def information(self):
        information = f"name = {self.name}, age={self.age},designation={self.designation}, salary = {self.salary}"

        return information

member1 = Political_Party("Narendra Modi", 66, "Prime Minister", 36000)

print(member1.name, "\n", member1.age, "\n", member1.designation, "\n", member1.salary)
print(member1.information())
member1.home_state("Gujarat")
member1.party("BJP")