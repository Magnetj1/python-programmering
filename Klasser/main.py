import random

class teacher:
    def __init__ (self,teacher_firstname, teacher_lastname,teacher_age, gender):
        self.teacher_firstname = teacher_firstname 
        self.teacher_lastname = teacher_lastname
        self.teacher_age = teacher_age
        self.gender = gender 
    def __str__(self):
        return f"{self.teacher_firstname} {self.teacher_lastname} {self.teacher_age}"
class student:
    def __init__ (self, firstname, lastname, student_age, gender):
        self.firstname = firstname 
        self.lastname = lastname
        self.student_age = student_age
        self.gender = gender 
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.student_age}"
class group:
    def __init__(self,subject,teacher,students):
        self.subject=subject
        self.teacher=teacher
        self.students=students

student_random_names=[
"seb",
"emanuel",
"nicklas",
"kazuma"
]
student_random_lastname=[
"satou",
"negro",
"näs",
"john"


]

teacher_random_names=[
"walter",
"Dream",
"gorelock",
"caseoh",
"trix",



]
teacher_random_lastnames=[
"white",
"jeas",
"Trex",
"bruva",

]

#credit to nick in our class he told me how it works
student1 = student(random.choice(student_random_names), random.choice(student_random_lastname), random.randint(14, 17), "Man")
student2 = student(random.choice(student_random_names), random.choice(student_random_lastname), random.randint(14, 17), "Man")
student3 = student(random.choice(student_random_names), random.choice(student_random_lastname), random.randint(14, 17), "Man")
student4 = student(random.choice(student_random_names), random.choice(student_random_lastname), random.randint(14, 17), "Man")
teacher1 = teacher(random.choice(teacher_random_names), random.choice(teacher_random_lastnames), random.randint(24,34),"Man")
print(teacher1,"\n","|",student1,"|",student2,"|",student3,"|",student4)
