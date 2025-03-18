import unittest
from student import student

class Test_student(unittest.TestCase):
    def test_student_initialization(self):
        student = student(1, "John Doe", "john.chris@.com", "password123")
        self.assertEqual(student.user_id, 1)
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.email, "john.chris@.com")
        self.assertEqual(student.password, "password123")
        self.assertEqual(student.courses, [])

    def test_view_courses(self):
        student = student(1, "John chris", "john.chris@.com", "password123")
        self.assertEqual(student.view_courses(), "You are not enrolled in any courses.")
        student.courses = ["Mathematics 101", "Physics 101"]
        self.assertEqual(student.view_courses(), ["Mathematics 101", "Physics 101"])

    def test_enroll_in_course(self):
        student = Student(1, "John chris", "john.chris@.com", "password123")
        student.enroll_in_course("Mathematics 101")
        self.assertEqual(student.courses, ["Mathematics 101"])
        student.enroll_in_course("Physics 101")
        self.assertEqual(student.courses, ["Mathematics 101", "Physics 101"])

