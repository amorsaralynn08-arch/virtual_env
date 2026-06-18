class Company:
    def __init__(self, director_name , shares , assets):
        self.director_name = director_name
        self._shares = shares
        self.__assets = assets      

class Staff(Company):
    def __init__(self , name ,department):
            self.name = name
            self.department = department
    def work_details(self , time_in , time_out):
       self.time_in = time_in
       self.time_out = time_out
    
            
employee1 = Staff("Barack" , "HR")
employee1.work_details("8AM" , "4PM")
employer1 = Company("Anna" , "2000" , "Land" )
print(f" Director {employer1.director_name} has {employer1._shares} shares ")

   