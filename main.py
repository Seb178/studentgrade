from student import Student
from classroom import Classroom
def main():

    print("Welcome to the student grade calculator")
    classroom = Classroom()

    while True:
        number_of_students = (input("Please enter number of students or q to quit: "))
        if number_of_students.lower() == "q":
            print("Exiting")
            break
        try:
            number_of_students = int(number_of_students)
            if number_of_students > 0:
                break
            else:
                print("Number must be greater than 0")
        except ValueError:
            print("Must be an integer")

    for i in range (number_of_students):
        name = input("Enter student name: ")
        student_object = Student(name)

        while True:
            try:
                num_modules = int(input(f"How many modules for {name}?: "))
                if num_modules > 0:
                    break
                else:
                    print("Must be greater than 0")
            except ValueError:
                print("Please enter a valid integer")
        
        for j in range(num_modules):
            while True:
                try:
                    mark = float(input(f"Enter mark for module {j+1}: "))
                    if 0 <= mark <= 100:
                        student_object.add_mark(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100")
                except ValueError:
                    print("Marks must be an integer")
        
        classroom.add_student(student_object)

    print("-----Student Results-----")
    for student in classroom.students:
        print(student)
    
    print(f"Class Average: {classroom.class_average(): .2f}")

    top = classroom.top_student()
    if top:
        print(f"Top student is {top.name}, with an average of: {top.average(): .2f} and a grade of {top.grade()}")


    classroom.export_to_csv("results.csv")
    print("Results exported to csv")


if __name__ == "__main__":
    main()
        
