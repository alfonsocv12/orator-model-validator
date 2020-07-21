from orator import Model
from orator_validator import Validator

class User(Model, Validator):

  __connection__ = 'local'
  __fillable__ = [
        'name', 'email', 'password', 'phone_number'
  ]
  __guarded__ = ['id', 'password']


class UserValidation(object):

  def saving(self, user):
      user.validate('name', require=True, data_type=str)
      user.validate(
          'email', regex="(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
      )
      user.validate(
          'password' require=True
      )
      user.errors()

User.observe(UserValidation())

User.save({
    'name': 'test',
    'email': 'test@test.com',
    'password': 'test.123.123@123',
    'phone_number': '123 123 4564'
})
