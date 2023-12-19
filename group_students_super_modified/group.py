from student import Student

class GroupCapacityError(Exception):
    def __init__(self, message="Group capacity exceeded"):
        self.message = message
        super().__init__(self.message)

class Group:
    MAX_CAPACITY = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < self.MAX_CAPACITY:
            self.group.add(student)
        else:
            raise GroupCapacityError()

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'
