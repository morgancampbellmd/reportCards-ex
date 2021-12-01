import sys
import json

from classes import course, exceptions, mark, student, test
import constants


if __name__ == '__main__':
    coursesFilename = sys.argv[1]
    studentsFilename = sys.argv[2]
    testsFilename = sys.argv[3]
    marksFilename = sys.argv[4]
    outputFilename = sys.argv[5]

    outputJson = {}

    with open(outputFilename, 'w') as outfile:

        # Process input files, deliver specific error output
        try:
            courseList = course.create_course_dict(coursesFilename)
            studentList = student.create_student_array(studentsFilename)
            testDict = test.create_test_dict(testsFilename)
            testsHaveValidWeights = test.validate_weights(testDict, courseList)
            markList = mark.create_mark_array(marksFilename, studentList, testDict)
        except exceptions.DuplicateCourseError:
            outputJson = constants.duplicate_course_error
        except exceptions.EmptyCourseDictError:
            outputJson = constants.empty_course_error
        except exceptions.DuplicateStudentError:
            outputJson = constants.duplicate_student_error
        except exceptions.EmptyStudentArrayError:
            outputJson = constants.empty_student_error
        except exceptions.DuplicateTestError:
            outputJson = constants.duplicate_test_error
        except exceptions.EmptyTestDictError:
            outputJson = constants.empty_test_error
        except exceptions.DuplicateMarkError:
            outputJson = constants.duplicate_mark_error
        except exceptions.EmptyMarkError:
            outputJson = constants.empty_mark_error
        except exceptions.MarkStudentMismatchError:
            outputJson = constants.mark_student_mismatch_error
        except exceptions.MarkTestMismatchError:
            outputJson = constants.mark_test_mismatch_error
        except exceptions.TestWeightError:
            outputJson = constants.test_weights_error
        except exceptions.TestCourseMismatchError:
            outputJson = constants.test_course_mismatch_error

        else:
            outputJson = {"students": []}
            for student in studentList:
                reportCard = []
                activeCourses = student.get_active_courses(courseList, testDict, markList)

                if len(activeCourses) > 0:
                    totalAverage = 0.00

                    for course in activeCourses:
                        courseAverage = student.get_score_for_course(testDict, markList, course)
                        reportCard.append({"id": int(course), "name": courseList[course].name,
                                           "teacher": courseList[course].teacher, "courseAverage": courseAverage})
                        totalAverage += courseAverage
                    totalAverage /= len(activeCourses)

                    outputJson["students"].append({"id": int(student.student_id), "name": student.name,
                                                   "totalAverage": round(totalAverage, 2), "courses": reportCard})
        json.dump(outputJson, outfile, indent=2)
