import warnings


def deprecated(callable_func):
    '''
    Deprecated decorator to print warning on deprecated functions

    param: callable_func
    ptype: function
    return: wrapper
    rtype: function
    '''
    warnings.warn_explicit(
        "{} function is deprecated".format(callable_func.__name__),
        category=DeprecationWarning,
        filename=callable_func.__code__.co_filenname,
        lineno=callable_func.__code__.co_firstlineno + 1
    )
    return callable_func


class ValidatorError(Exception):
    """Raised when the validator find and error"""

    def __init__(self, status_code=None, body=None):
        self.status_code = status_code
        self.body = body
