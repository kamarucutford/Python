
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        return super().__str__() + f", Required for Major: {self.required_for_major}"


class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return super().__str__() + f", Elective Type: {self.elective_type}"


core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("CS202", "Artificial Intelligence", 3, "Technical")

print(core_course)
print(elective_course)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary
from employee import Employee

# Create an Employee object
emp = Employee("Kamarudheen", 150000)

# Display the employee's name and salary
print("Employee Name:", emp.get_name())
print("Employee Salary:", emp.get_salary())
