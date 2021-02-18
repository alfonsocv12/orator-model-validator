def deprecated(callable_obj):
    def wrapper(callable_obj):
        print(callable_obj)
        return callable_obj
    return wrapper

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValidatorError(Error):
    """Raised when the validator find and error"""

    def __init__(self, status_code=None, body=None):
        self.status_code = status_code
        self.body = body
