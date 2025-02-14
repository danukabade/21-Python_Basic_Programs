class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn
        self.marks = []
        self.total = 0

    def getMarks(self):
        for i in range(3):
            marks = float(input(f"Enter marks for subject {i + 1}: "))
            self.marks.append(marks)
            self.total += marks

    def display(self):
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Marks:")
        for i in range(3):
            print(f"\tSubject {i + 1}: {self.marks[i]}")
        print("Total:", self.total)
        print("Percentage:", round((self.total / 3), 2))


# Main program
name = input("Enter name: ")
usn = input("Enter USN: ")
student = Student(name, usn)
student.getMarks()
student.display()
