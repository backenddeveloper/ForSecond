'''
'''


class ValidationException(Exception):

    def __init__(self, message=''):

        self.message = message


class InvalidGraphException(ValidationException):

    pass
