import re
import time
import json
from switch import Switch
from .errors import (
    deprecated, ValidatorError
)

class Validator(object):

    __errors__ = {'code':200, 'errors':[]}

    def validate(self, key, **kwarg):
        '''
        Function dedicated to validate input to a model

        #####
        '''
        if len(kwarg) > 1:
            raise ValidatorError(
                500,
                json.dumps({
                    'code':500, 'errors':['More than one arg on validation']
                })
            )
        with Switch(kwarg):
            if case()

    @classmethod
    def __handle_error(cls, type_error, value_name,
            custom_msg=False, custom_error=False, **args):
        '''
        Funtion dedicated to handle errors on the validation

        param: str type_error: this is use for the default msg
        param: str value_name: this is use for the default msg
        param: str custom_msg: is they want to use a custom_msg
        param: function custom_error: Optional to send a custom error
        param: args **args: Values of the custom error
        return: None
        '''
        if custom_error:
            custom_error(**args)
        cls.add_error(code=400, msg=custom_msg
                if custom_msg else
                'Error of {} on {}'.format(type_error, value_name)
        )

    @classmethod
    def errors(cls, validation_init=True):
        '''
        Function dedicated to delete errors after use

        param: validation_init
        ptype: volean
        return: __errors__
        rtype: dict
        '''
        errors = cls.__errors__
        cls.__errors__ = {'code':200, 'errors':[]}
        if errors['code'] != 200:
            raise ValidatorError(errors['code'], json.dumps(errors['errors']))

    @classmethod
    def add_error(cls, code=None, msg=None):
        '''
        Function dedicated to modify errors

        param: int code: The error code that we will return
        param: str msg: the msg to append to error list
        '''
        if code:
            cls.__errors__['code'] = code
        if msg:
            cls.__errors__['errors'].append({
                'msg': msg
            })
