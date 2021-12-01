import unittest

from classes import exceptions, mark, student, test


class MarkUnitTests(unittest.TestCase):
    def test_create_marks_array_duplicates(self):
        studentArray = student.create_student_array("resources/valid_students.csv")
        testDict = test.create_test_dict("resources/valid_tests.csv")
        self.assertRaises(exceptions.DuplicateMarkError, mark.create_mark_array,
                          "resources/marks_with_duplicates.csv", studentArray, testDict)

    def test_create_mark_array_empty(self):
        studentArray = student.create_student_array("resources/valid_students.csv")
        testDict = test.create_test_dict("resources/valid_tests.csv")
        self.assertRaises(exceptions.EmptyMarkError, mark.create_mark_array,
                          "resources/empty_marks.csv", studentArray, testDict)

    def test_create_mark_array_mark_student_mismatch(self):
        studentArray = student.create_student_array("resources/valid_students.csv")
        testDict = test.create_test_dict("resources/valid_tests.csv")
        self.assertRaises(exceptions.MarkStudentMismatchError, mark.create_mark_array,
                          "resources/marks_with_nonexistent_student.csv", studentArray, testDict)

    def test_create_mark_array_mark_test_mismatch(self):
        studentArray = student.create_student_array("resources/valid_students.csv")
        testDict = test.create_test_dict("resources/valid_tests.csv")
        self.assertRaises(exceptions.MarkTestMismatchError, mark.create_mark_array,
                          "resources/marks_with_nonexistent_test.csv", studentArray, testDict)


    def test_create_mark_array_valid(self):
        studentArray = student.create_student_array("resources/valid_students.csv")
        testDict = test.create_test_dict("resources/valid_tests.csv")
        markArray = mark.create_mark_array("resources/valid_marks.csv", studentArray, testDict)
        self.assertEqual(markArray[0].test_id, "1")
        self.assertEqual(markArray[0].student_id, "1")
        self.assertEqual(markArray[0].score, "78")
        self.assertEqual(markArray[1].test_id, "2")
        self.assertEqual(markArray[1].student_id, "1")
        self.assertEqual(markArray[1].score, "87")
        self.assertEqual(markArray[2].test_id, "3")
        self.assertEqual(markArray[2].student_id, "1")
        self.assertEqual(markArray[2].score, "95")
