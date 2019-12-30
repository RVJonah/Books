from werkzeug.security import check_password_hash

def login_user(user_data, Users, database, session):
    username = user_data['username']
    user_is_found = database.query(Users).filter_by(username=username).all()
    if user_is_found == []:
        return {'error': 'Username or Password incorrect'}
    if check_password_hash(user_is_found[0].password_hash, user_data['password']):
        if 'check' in user_data:
            return True
        session['user_id'] = username
        return True  
    return {'error': 'Username or Password incorrect'}