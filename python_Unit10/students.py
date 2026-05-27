class Student:
    id = "No ID"
    name = "Students"
    credits = 0
    gpa = 0.0
    
def print_student(student):
    print("Student:", student.id, student.name, student.credits, student.gpa)

def main():
    student1 = Student()
    student2 = Student()
    
    student1.id = "1234"
    student1.name = "Callie"
    student1.credits = 89
    student1.gpa = 3.7
    
    student2.id = "5678"
    student2.name = "Taehun"
    student2.credits = 39
    student2.gpa = 3.5
    
    print_student(student1)
    print_student(student2)
    

    
if __name__ == "__main__":
    main()
    
    
    
