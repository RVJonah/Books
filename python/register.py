from werkzeug.security import generate_password_hash
from sqlalchemy import desc

def is_user_unique(username, Users, database):
  username_query_result = database.query(Users).filter_by(username=username)
  if username_query_result.count() > 0:
    return False
  return True

def register_user(user_data, Users, database):
  user_is_unique = is_user_unique(user_data['username'], Users, database)
  if not user_is_unique:
    return {'error': 'Username is already taken'}
  if user_data['password'] != user_data['confirmPassword']:
    return {'error': "password fields do not match"}
  if user_data['email'] != user_data['confirmEmail']:
    return {'error': "email fields do not match"}
  password_hash = generate_password_hash(user_data['password'])
  username = user_data['username']
  email = user_data['email']
  if user_is_unique:
    if "check" in user_data:
      return True
    new_user = Users(username, password_hash, email)
    database.add(new_user)
    database.commit()
    return True
  return False