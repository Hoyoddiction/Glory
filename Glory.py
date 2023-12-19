import json

class Course:
    def __init__(self, code, title, capacity):
        self.code = code
        self.title = title
        self.capacity = capacity
        self.enrolled_students = []

    def available_slots(self):
        return self.capacity - len(self.enrolled_students)

    def enroll_student(self, student):
        if self.available_slots() > 0:
            self.enrolled_students.append(student)
            return True
        else:
            return False

    def display_details(self):
        print(f"Course Code: {self.code}\nTitle: {self.title}\nCapacity: {self.capacity}\nEnrolled Students: {len(self.enrolled_students)}")

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses_enrolled = []

    def enroll_in_course(self, course):
        if course.enroll_student(self):
            self.courses_enrolled.append(course.code)
            return True
        else:
            return False

    def display_info(self):
        print(f"Student ID: {self.student_id}\nName: {self.name}\nCourses Enrolled: {', '.join(self.courses_enrolled)}")

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def main():
    courses_data = load_data('courses.json')
    students_data = load_data('students.json')

    # Create Course instances
    course1 = Course("CSE101", "Introduction to Computer Science", 30)
    course2 = Course("MAT202", "Calculus II", 25)

    courses = [course1, course2]

    # Create Student instances
    student1 = Student("S001", "John Doe")
    student2 = Student("S002", "Jane Doe")

    students = [student1, student2]

    # Enroll students in courses
    student1.enroll_in_course(course1)
    student2.enroll_in_course(course1)
    student2.enroll_in_course(course2)

    # Display course details and student information
    for course in courses:
        course.display_details()

    for student in students:
        student.display_info()

    # Save data to files
    save_data([course.__dict__ for course in courses], 'courses.json')
    save_data([student.__dict__ for student in students], 'students.json')

if __name__ == "__main__":
    main()

