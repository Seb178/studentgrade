import os
import csv
from student import Student


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def class_average(self):
        if not self.students:
            return 0
        else:
            return sum(s.average() for s in self.students) / len(self.students)
        
    def top_student(self):
        if not self.students:
            return None
        top = self.students[0]
        for s in self.students:
            if s.average() > top.average():
                top = s
        return top
    

    def sort_by_average(self):
        sorted_students = self.students[:]

        def get_average(student):
            return student.average()
        
        sorted_students.sort(key = get_average, reverse = True)

        return sorted_students
    
    def export_to_csv(self, filename="results.csv"):

        folder = "output"

        if not os.path.exists(folder):
            os.makedirs(folder)

        file_path = os.path.join(folder, filename)

        sorted_students = self.sort_by_average()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Rank", "Name", "Average", "Grade"])
            for rank, student in enumerate(sorted_students, start=1):
                writer.writerow([rank, student.name, f"{student.average():.2f}", student.grade()])
        print(f"CSV saved at {file_path}")