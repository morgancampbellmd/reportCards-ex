import unittest
from classes import course, exceptions, mark, student, test


class StudentUnitTests(unittest.TestCase):
    def test_create_student_array_duplicates(self):
        self.assertRaises(exceptions.DuplicateStudentError, student.create_student_array, "resources/students_with_duplicates.csv")

    def test_create_student_array_empty(self):
        self.assertRaises(exceptions.EmptyStudentArrayError, student.create_student_array, "resources/empty_students.csv")

    def test_create_student_array_valid(self):
        studentArray = student.create_student_array("resources/valid_students.csv")
        self.assertEqual(studentArray[0].student_id, "1")
        self.assertEqual(studentArray[0].name, "A")
        self.assertEqual(studentArray[1].student_id, "2")
        self.assertEqual(studentArray[1].name, "B")
        self.assertEqual(studentArray[2].student_id, "3")
        self.assertEqual(studentArray[2].name, "C")

    def test_get_active_courses_valid(self):
        courseDict = course.create_course_dict("resources/valid_courses.csv")
        studentArray = student.create_student_array("resources/valid_students.csv")
        testDict = test.create_test_dict("resources/valid_tests.csv")
        markArray = mark.create_mark_array("resources/valid_marks.csv", studentArray, testDict)

        activeCourses = studentArray[1].get_active_courses(courseDict, testDict, markArray)

        self.assertEqual(activeCourses, ['1', '3'])

    def test_get_active_courses_none(self):
        courseDict = course.create_course_dict("resources/valid_courses.csv")
        studentArray = student.create_student_array("resources/valid_students.csv")
        testDict = test.create_test_dict("resources/valid_tests.csv")
        markArray = mark.create_mark_array("resources/valid_marks.csv", studentArray, testDict)

        activeCourses = studentArray[3].get_active_courses(courseDict, testDict, markArray)

        self.assertEqual(activeCourses, [])

    def test_get_score_for_course_valid(self):
        studentArray = student.create_student_array("resources/valid_students.csv")
        testDict = test.create_test_dict("resources/valid_tests.csv")
        markArray = mark.create_mark_array("resources/valid_marks.csv", studentArray, testDict)

        courseAverage = studentArray[0].get_score_for_course(testDict, markArray, "3")

        self.assertEqual(courseAverage, 74.2)


if __name__ == '__main__':
    unittest.main()
