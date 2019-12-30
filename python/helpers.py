from flask import redirect, session, current_app
from functools import wraps

def login_required(route):
    # creates login required routes
    @wraps(route)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return route(*args, **kwargs)
    return decorated_function

def is_data_present(data):
  empty_fields = []
  for key, value in data.items():
    if value == "":
      empty_fields.append(key)
  return empty_fields

  