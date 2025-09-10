class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Student Name :", self.name)
        print("Roll Number  :", self.roll_no)


# Main Program
name = input("Enter student name: ")
roll = input("Enter roll number: ")

s1 = Student(name, roll)
print("\n--- Student Information ---")
s1.display()
