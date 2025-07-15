# Exercício 2

class students:
    def __init__(self,name,grade):
        self.name = name
        self.grade = int(grade)

    def get_name(self):
        return self.name
    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def __repr__(self):
        return "Student {} in grade {} was added.".format(self.name, self.grade)

    list_grade = []
    list_names = []
    def add_student(self):
        self.list_grade.append(self.grade)
        self.list_grade.sort()
        # self.list_names.append(self.name) by grade sorted
        for i in range(len(self.list_grade)):
            if self.grade == self.list_grade[i]: # self.list_names.append(self.name)
                # Find insertion point to maintain alphabetical order within same grade
                insert_pos = i
                while insert_pos < len(self.list_names) and self.list_grade[insert_pos] == self.grade and self.name > self.list_names[insert_pos]:
                    insert_pos += 1
                self.list_names.insert(insert_pos, self.name)
                break
        return self.list_names

s1 = students("Murphy", 1)
print(s1)
s2 = students("Vivian", 2)
s3 = students("Charlie", 5)
s4 = students("Alice", 2)
s5 = students("Carlos", 2)
s1.add_student()
s2.add_student()
s3.add_student()
s4.add_student()
s5.add_student()
print(students.list_grade)
print(students.list_names)