#private and public attributes
#getter and setter

class DataScientist:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_of_bugs_solved = 0
    
    #salary factor
    def code(self):
        self._num_of_bugs_solved += 1     
    #getter
    def get_salary(self):
        return self._salary
    #setter
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_of_bugs_solved < 10:
            return base_value

        if self._num_of_bugs_solved <100:
            return base_value * 2
        else:
            return base_value * 3

ds = DataScientist("Sonu", 24)
print(ds.age, ds.name)

for i in range(70):
    ds.code()

ds.set_salary(20000)
print(ds.get_salary())

