import constants


class DuplicateCourseError(BaseException):
    def __init__(self):
        super().__init__()


class EmptyCourseDictError(BaseException):
    def __init__(self):
        super().__init__()


class DuplicateStudentError(BaseException):
    def __init__(self):
        super().__init__()


class EmptyStudentArrayError(BaseException):
    def __init__(self):
        super().__init__()


class DuplicateTestError(BaseException):
    def __init__(self):
        super().__init__()


class TestWeightError(BaseException):
    def __init__(self):
        super().__init__()


class TestCourseMismatchError(BaseException):
    def __init__(self):
        super().__init__()


class EmptyTestDictError(BaseException):
    def __init__(self):
        super().__init__()


class DuplicateMarkError(BaseException):
    def __init__(self):
        super().__init__()


class EmptyMarkError(BaseException):
    def __init__(self):
        super().__init__()


class MarkTestMismatchError(BaseException):
    def __init__(self):
        super().__init__()


class MarkStudentMismatchError(BaseException):
    def __init__(self):
        super().__init__()