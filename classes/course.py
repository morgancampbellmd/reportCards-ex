import csv
from classes import exceptions


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


def create_course_dict(courseFilename):
    courseDict = {}

    with open(courseFilename, 'r', newline='') as courseCsv:
        courseReader = csv.DictReader(courseCsv, delimiter=',')

        for row in courseReader:

            # Check if id already exists, break if found
            if row["id"] in courseDict:
                raise exceptions.DuplicateCourseError

            courseDict[row["id"]] = Course(row["name"].strip(), row["teacher"].strip())

    # Check if empty course file was received, break if true
    if not courseDict:
        raise exceptions.EmptyCourseDictError

    return courseDict
