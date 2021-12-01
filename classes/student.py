import csv
from classes import exceptions


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_active_courses(self, courseDict, testDict, markList):
        activeCourseList = []

        for course in courseDict:
            for mark in markList:
                if testDict[mark.test_id].course_id == course and mark.student_id == self.student_id:
                    activeCourseList.append(course)
                    break

        return activeCourseList

    def get_score_for_course(self, testDict, markList, course):
        courseMark = 0.0

        for mark in markList:
            if testDict[mark.test_id].course_id == course and mark.student_id == self.student_id:
                courseMark += (int(mark.score) * int(testDict[mark.test_id].weight))/100

        return round(courseMark, 1)


def create_student_array(studentFilename):
    studentArray = []

    with open(studentFilename, 'r', newline='') as studentCsv:
        studentReader = csv.DictReader(studentCsv, delimiter=',')

        for row in studentReader:
            if any(student.student_id == row["id"] for student in studentArray):
                raise exceptions.DuplicateStudentError

            studentArray.append(Student(row["id"], row["name"].strip()))

    studentArray.sort(key=lambda x: x.student_id)

    if not studentArray:
        raise exceptions.EmptyStudentArrayError

    return studentArray
