# More Classes and OOP in Python
Use your knowledge of Python Classes to create a homework tracker!

Create your classes in the provided `classroom.py` file.

## Exercise: Write the following classes
Let's practice writing classes with useful functionalities

* Create an **Assignment** class
  * Assignments have `name`, `github_url`, `completed`, and `grade` properties
  * `completed`'s initial value should be set to `False`
  * `grade`'s initial value should be set to `None`
  * Assignments have a `mark_done` method that take in the grade as an argument, and sets `grade` and `completed`

* Create a **Student** class
  * Students have `name`, `pending_homeworks` and `completed_homeworks` properties
  * Students have a `assign_homework` method
  * Students have a `complete_homework` method 
  * Students have a `print_outstanding_homeworks` method
  * The `assign_homework` method takes in an `Assignment` object, and adds it to its `pending_assignments` list
  * The `complete_homework` method takes in the name of the homework, and the grade as an argument. It finds the specified homework in the `pending_homeworks` list and calls it's `mark_done` method. The method removes the `Assignment` from `pending_homeworks` and adds it to `completed_homeworks` 
    * Returns `True` if assignment was found and modified, `False` if not found
  * `print_outstanding_homeworks` prints out the name of each of the `pending_homeworks`


* Create a **SeiClass** class
  * SeiClass has `name`, and `students` properties
  * SeiClass has an `add_student` method that takes in a `Student` object
  * SeiClass has an `assign_homework` method that takes in an `Assignment` object and assigns that assignment to every student
  * BONUS - What would need to be changed in our classes to facilitate a `print_avg_grade` function? Implement it!

    
Sample Input:

```py
nick = Student('Nick')
sarah = Student('Sarah')
brandi = Student('Brandi')

sei30 = SeiClass('sei30')
sei30.add_student(nick)
sei30.add_student(sarah)
sei30.add_student(brandi)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei30.assign_homework(assignment1)

nick.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

nick.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
brandi.print_outstanding_homeworks()
```

Sample Output

```
Nick has no outstanding homeworks!
Sarah has no outstanding homeworks!
Brandi still needs to turn in: Bounty Hunters
```
