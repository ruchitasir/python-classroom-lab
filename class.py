import copy
class Assignment:
    def __init__(self, name, github_url):
        self.name = name
        self.github_url = github_url
        self.completed = False
        self.grade = None
    def mark_done(self, grade):
        self.grade = grade
        self.completed = True
class Student:
    def __init__(self, name):
        self.name = name
        self.pending_homeworks = []
        self.completed_homeworks = []
    def assign_homework(self, assignment):
        self.pending_homeworks.append(assignment)
    def complete_homework(self, assignName, grade):
        for assign in self.pending_homeworks:
            if assign.name == assignName: 
                assign.mark_done(grade)
                self.completed_homeworks.append(assign)
                self.pending_homeworks.remove(assign)
    def print_outstanding_homeworks(self):
        for assign in self.pending_homeworks: 
            print(f"Assignment outstanding for {self.name}: {assign.name}")
class SeiClass:
    def __init__(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def assign_homework(self, assign):
        for each in self.students:
            each.assign_homework(copy.deepcopy(assign))
    def get_students_grade(self, student):
        sumScores = 0
        for each in student.completed_homeworks:
            sumScores += each.grade
        try:
            grade = sumScores / len(student.completed_homeworks)
            print(f"Grade average for {student.name}: {grade}") 
            return grade
        except:
            return None
    def print_avg_grade(self):
        sumScores = 0
        studentsWithGrades = 0
        for each in self.students:
            studentAvg = self.get_students_grade(each)
            if (studentAvg != None): 
                sumScores += studentAvg
                studentsWithGrades += 1
        print("Average Score:", (sumScores/studentsWithGrades))
henry = Student('Henry')
sarah = Student('Sarah')
mike = Student('Mike')
print(f"""Student:
    Name: {henry.name}
    Pending: {henry.pending_homeworks}
    Completed: {henry.completed_homeworks}""")
sei26 = SeiClass('sei26')
sei26.add_student(henry)
sei26.add_student(sarah)
sei26.add_student(mike)
assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')
print(f"""Assignment 1: 
    Name: {assignment1.name} 
    Url: {assignment1.github_url} 
    Completed: {assignment1.completed} 
    Grade: {assignment1.grade}""")
print("Assigned a homework to the class")
sei26.assign_homework(assignment1)
print(f"""Student:
    Name: {henry.name}
    Pending: {henry.pending_homeworks}
    Completed: {henry.completed_homeworks}""")
print(f"""Student:
    Name: {sarah.name}
    Pending: {sarah.pending_homeworks}
    Completed: {sarah.completed_homeworks}""")
henry.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)
henry.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
mike.print_outstanding_homeworks()
sei26.print_avg_grade()