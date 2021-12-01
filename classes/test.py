import csv
from classes import exceptions


class Test:
    def __init__(self, course_id, weight):
        self.course_id = course_id
        self.weight = weight


def create_test_dict(testsFilename):
    testDict = {}

    with open(testsFilename, 'r', newline='') as testCsv:
        testReader = csv.DictReader(testCsv, delimiter=',')

        for row in testReader:

            # Check for duplicate test_id, break if found
            if row["id"] in testDict:
                raise exceptions.DuplicateTestError

            testDict[row["id"]] = Test(row["course_id"], row["weight"])

    # Check if empty test file received
    if not testDict:
        raise exceptions.EmptyTestDictError

    return testDict


def validate_weights(testDict, courseDict):
    courseWeights = {}

    for course in courseDict:
        courseWeights.update({course: "0"})

    for test in testDict.values():
        try:
            courseWeights[test.course_id] = int(courseWeights[test.course_id]) + int(test.weight)

        # Check if test uses a non-existent course_id, break if found
        except KeyError:
            raise exceptions.TestCourseMismatchError

    # Check if course weights don't add up to 100, break if true
    for course in courseWeights:
        if courseWeights[course] != 100:
            raise exceptions.TestWeightError

    return True
