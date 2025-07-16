# Exercício 2

# Students Class created to receive name and grade
class students:
    list_students = []
    def __init__(self,name,grade):
        self.name = name
        self.grade = int(grade)
        students.list_students.append((self.grade, self.name))

    def get_name(self):
        return self.name
    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def __repr__(self):
        return "Student {} in grade {} was added.".format(self.name, self.grade)

    def sort_students(self):
        sorted_list = sorted(students.list_students, key=lambda x: (x[0], x[1]))
        return [x[1] for x in sorted_list]

s1 = students("Murphy", 1)
print(s1)
s2 = students("Vivian", 2)
s3 = students("Charlie", 5)
s4 = students("Alice", 2)
s5 = students("Carlos", 2)
s1.sort_students()
s2.sort_students()
s3.sort_students()
s4.sort_students()
s5.sort_students()
print(s1.sort_students())