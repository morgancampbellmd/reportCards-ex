import unittest

from classes import course, exceptions


class MyTestCase(unittest.TestCase):
    def test_create_marks_array_duplicates(self):
        self.assertRaises(exceptions.DuplicateCourseError, course.create_course_dict, "resources/courses_with_duplicates.csv")

    def test_create_test_dict_empty(self):
        self.assertRaises(exceptions.EmptyCourseDictError, course.create_course_dict, "resources/empty_courses.csv")

    def test_create_test_dict_valid(self):
        courseDict = course.create_course_dict("resources/valid_courses.csv")
        self.assertEqual(courseDict["1"].name, "Biology")
        self.assertEqual(courseDict["1"].teacher, "Mr. D")
        self.assertEqual(courseDict["2"].name, "History")
        self.assertEqual(courseDict["2"].teacher, "Mrs. P")
        self.assertEqual(courseDict["3"].name, "Math")
        self.assertEqual(courseDict["3"].teacher, "Mrs. C")


if __name__ == '__main__':
    unittest.main()
