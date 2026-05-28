class Student:

    __slots__ = ["id", "name", "credits", "gpa"]

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0.0
    
def print_student(student):
    print("Student:", student.id, student.name, student.credits, student.gpa)

def main():
    # student1 = Student()
    # student2 = Student()
    
    # student1.id = "1234"
    # student1.name = "Callie"
    # student1.credits = 89
    # student1.gpa = 3.7
    
    # student2.id = "5678"
    # student2.name = "Taehun"
    # student2.credits = 39
    # student2.gpa = 3.5
    
    # print_student(student1)
    # print_student(student2)
    callie = Student("1234", "Callie")
    tae = Student("4567", "Taehun")
    print_student(callie)
    print_student(tae)

    
if __name__ == "__main__":
    main()
    
    
    
