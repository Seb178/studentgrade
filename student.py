class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
    
    def add_mark(self, mark: float):
        if 0 <= mark <= 100:
            self.marks.append(mark)
        else:
            raise ValueError("Marks must be between 0 and 100")
        
    def average(self):
        if not self.marks:
            return 0
        else:
            return sum(self.marks) / len(self.marks)
        
    def grade(self):
        avg = self.average()
        if avg == 0:
            return "No marks"
        elif avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "Fail"
        
    def __str__(self):
        return f"{self.name} Average: {self.average(): .2f}, Grade: {self.grade()}"
    
