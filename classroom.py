import copy

class Assignment:
    def __init__(self, name, github_url,completed=False,grade=None):
          self.name = name
          self.github_url = github_url
          self.completed = completed
          self.grade = grade
       
    def mark_done(self,grade):
         self.grade = grade
         self.completed = True
  

class Student:
    def __init__(self, name):
           self.name = name
           self.pending_homeworks = []
           self.completed_homeworks = []  
        

    def assign_homework(self,assignment):
         # print(f'number of HWs for {self.name} is {len(self.pending_homeworks)}')  
          print(f'{assignment} is given to {self.name} assign_homework of student is called')
          self.pending_homeworks.append(copy.deepcopy(assignment))

    def complete_homework(self, assignment_name, grade ):
            #assignment_done = {} 
            found = False
            for hw in  self.pending_homeworks:
               if(hw.name == assignment_name):
                   hw.mark_done(grade)
                   #assignment_done = hw
                   self.pending_homeworks.remove(hw) 
                   self.completed_homeworks.append(hw) 
                   found = True
            # if(found):        
            #     self.pending_homeworks.pop(assignment_done) 
            #     self.completed_homeworks.append(assignment_done) 
            return found      

    def print_outstanding_homeworks(self):
        print(f'number of HWs {len(self.pending_homeworks)}')
        for hw in  self.pending_homeworks:
            print(f'Pending HWs for{self.name} is {hw.name}')

       
   

class SeiClass:
    def __init__(self, name, students=[]):
        self.name = name
        self.students = students

    def add_student(self,student):
        self.students.append(student)

    def assign_homework(self, assignment):
        for student in self.students:
            print(f'{student.name} is assigned {assignment.name}')
            student.assign_homework(assignment)

    def getAllStudents(self):
            for student in self.students:
                 print(f'{student.name} is in class {self.name}')    


nick = Student('Nick')
sarah = Student('Sarah')
brandi = Student('Brandi')

sei30 = SeiClass('sei30')
sei30.add_student(nick)
sei30.add_student(sarah)
sei30.add_student(brandi)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei30.assign_homework(assignment1)

# nick.complete_homework('Bounty Hunters', 98)
# sarah.complete_homework('Bounty Hunters', 95)

nick.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
brandi.print_outstanding_homeworks()


