import csv
from classes import exceptions


class Mark:
    def __init__(self, test_id, student_id, score):
        self.test_id = test_id
        self.student_id = student_id
        self.score = score


def create_mark_array(markFilename, studentList, testDict):

    markArray = []

    with open(markFilename, 'r', newline='') as studentCsv:
        markReader = csv.DictReader(studentCsv, delimiter=',')

        for row in markReader:

            # Check for duplicated marks for the same test and student, break if found
            if any(mark.test_id == row["test_id"] and mark.student_id == row["student_id"] for mark in markArray):
                raise exceptions.DuplicateMarkError

            # Check for marks without an associated student, break if found
            elif not any(row["student_id"] == student.student_id for student in studentList):
                raise exceptions.MarkStudentMismatchError

            # Check for marks without an associated test, break if found
            elif row["test_id"] not in testDict:
                raise exceptions.MarkTestMismatchError

            else:
                markArray.append(Mark(row["test_id"], row["student_id"], row["mark"]))

    # Check if empty mark file was received
    if not markArray:
        raise exceptions.EmptyMarkError

    return markArray

