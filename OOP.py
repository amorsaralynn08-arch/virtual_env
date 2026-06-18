class Student:
    curreny = "ksh"
    def __init__(self , name ,  course):
        self.name = name
        self.course = course

    def study(self  , time , level ):
       self.time = time
       self.level = level
        



    @classmethod
    def grade(cls , score):
     cls.score = score
     print(f"students paying with a currency of {Student.currency}shld score {cls.score}")

student1 = Student("Abel" , "Python")
student1.study("7 hours" , "beginner")
        
student2 = Student("miles" , "Django" )
student2.study("3 hours" , "pro")
print(f"{student1.name} takes {student1.time} to study {student1.course}  ")
print(f"{student2.name} takes {student2.time} to study {student2.course}  ")

student1.cohort = "26M"
Student.cohort = "34Z"
# print("\n" , dir(student1))
# print("\n" , dir(Student))
print(student1)
print(Student)