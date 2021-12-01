import unittest

from classes import course, exceptions, test


class TestUnitTests(unittest.TestCase):
    def test_create_marks_array_duplicates(self):
        self.assertRaises(exceptions.DuplicateTestError, test.create_test_dict, "resources/tests_with_duplicates.csv")

    def test_create_test_dict_empty(self):
        self.assertRaises(exceptions.EmptyTestDictError, test.create_test_dict, "resources/empty_tests.csv")

    def test_create_test_dict_valid(self):
        testDict = test.create_test_dict("resources/valid_tests.csv")
        self.assertEqual(testDict["1"].course_id, "1")
        self.assertEqual(testDict["1"].weight, "10")
        self.assertEqual(testDict["2"].course_id, "1")
        self.assertEqual(testDict["2"].weight, "40")
        self.assertEqual(testDict["3"].course_id, "1")
        self.assertEqual(testDict["3"].weight, "50")
        self.assertEqual(testDict["4"].course_id, "2")
        self.assertEqual(testDict["4"].weight, "40")

    def test_validate_test_weights_valid(self):
        testDict = test.create_test_dict("resources/valid_tests.csv")
        courseDict = course.create_course_dict("resources/valid_courses.csv")

        weightsAreValid = test.validate_weights(testDict, courseDict)

        self.assertTrue(weightsAreValid)

    def test_validate_test_weights_invalid_weights(self):
        testDict = test.create_test_dict("resources/tests_with_bad_weights.csv")
        courseDict = course.create_course_dict("resources/valid_courses.csv")

        self.assertRaises(exceptions.TestWeightError, test.validate_weights, testDict, courseDict)

    def test_validate_test_weights_course_mismatch(self):
        testDict = test.create_test_dict("resources/tests_with_nonexistent_course.csv")
        courseDict = course.create_course_dict("resources/valid_courses.csv")

        self.assertRaises(exceptions.TestCourseMismatchError, test.validate_weights, testDict, courseDict)
