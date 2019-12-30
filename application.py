import requests
import json
from flask import Flask, jsonify, redirect, render_template, request, session, url_for, make_response
from flask_session import Session
from sqlalchemy.orm import sessionmaker
from .database import initiate_database
from .python import login_required, login_user, is_user_unique, register_user, is_data_present, book_search, sql_results_to_dict, add_change_review, delete_review, get_review, add_goodreads_data
app = Flask(__name__)
database = initiate_database()

# Configure session to use filesystem
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
db_session = sessionmaker(database['engine'])
db = db_session()
Books = database['books']
Users = database['users']
Reviews = database['reviews']

@app.route('/')
def index_route():
  return render_template('index.html', session=session)

@app.route('/register', methods=['GET', 'POST'])
def register_route():
  if request.method == 'POST':
    user_data = request.form.to_dict()
    empty_fields = is_data_present(user_data)
    if not empty_fields:
      user_is_registered = register_user(user_data, Users, db)
      if 'check' in user_data:
        return jsonify(user_is_registered)
      if user_is_registered:
        session['user_id'] = user_data['username']
        return redirect(url_for('search_route'))
    return jsonify(empty_fields)   
  return render_template('register.html', session=session), 200

@app.route('/login', methods=['GET', 'POST'])
def login_route():
  if request.method == 'POST':
    user_data = request.form.to_dict()
    empty_fields = is_data_present(user_data)
    if not empty_fields:
        login_successful = login_user(user_data, Users, db, session)
        if 'check' in user_data:
          return jsonify(login_successful)
        if login_successful == True:
            return redirect(url_for('search_route'), 302)
        return jsonify(login_successful)
    return jsonify(empty_fields)
  return render_template('login.html', session=session)

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search_route():
  if request.method == 'POST':
    search_term = request.form.get('searchText')
    search_type = request.form.get('searchType')
    search_results = book_search(db, Books, search_term, search_type)
    if search_results == False:
      return jsonify({'error': 'Sorry, No books found'})
    search_results = sql_results_to_dict(search_results)
    return jsonify(search_results), 200
  return render_template('search.html', session=session)

@app.route('/logout')
def logout_route():
  session.clear()
  return redirect(url_for('index_route'), 302)

@app.route('/book')
@login_required
def book_route():
  search_term = request.args.get('isbn')
  books_data = book_search(db, Books, search_term, 'ISBN')
  books_data = sql_results_to_dict(books_data)[0]
  books_data = add_goodreads_data(books_data, search_term)
  user_review_data = get_review(db, Reviews, search_term, session['user_id'])
  if user_review_data != []:
    user_review_data = user_review_data[0]
  all_reviews = get_review(db, Reviews, search_term)
  session['current_book'] = search_term
  return render_template('book.html', book=books_data, review=user_review_data, all_reviews=all_reviews), 200

@app.route('/review', methods=['POST', 'DELETE'])
@login_required
def review_route():
  if request.method == 'POST':
    review_data = request.form
    review_response = add_change_review(db, Reviews, review_data, session)
    return jsonify(review_response), 200
  if request.method == 'DELETE':
    review_response = delete_review(db, Reviews, session['current_book'], session['user_id'])
    return jsonify(review_response), 200

@app.route('/api/<string:isbn>')
def book_api(isbn):
  book = book_search(db, Books, isbn, 'ISBN')
  if book == False:
    return make_response(jsonify({'error': 'Sorry no book found'}), 404)
  book = sql_results_to_dict(book)[0]
  add_goodreads_data(book, isbn)
  return jsonify(book), 200

if __name__ == "__main__":
    app.run(ssl_context='adhoc')