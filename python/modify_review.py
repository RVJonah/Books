from sqlalchemy import func

def delete_review(db, Reviews, isbn, username):
		review = db.query(Reviews).filter_by(username=username, isbn=isbn).first()
		if review == None:
				return {'message': "No review to delete"}
		db.query(Reviews).filter_by(username=username, isbn=isbn).delete()
		db.commit()
		return {'message': "Review deleted"}

def add_change_review(db, Reviews, review_data, session):
		isbn = session['current_book']
		username = session['user_id']
		review_title = review_data['review_title']
		review_text = review_data['review_text']
		review_rating = review_data['review_rating']
		review = db.query(Reviews).filter_by(username=username, isbn=isbn).first()
		if review == None:
				review_number = db.query(func.max(Reviews.review_number)).scalar()
				print(review_number)
				if review_number == None:
					review_number = 1
				else:
					review_number +=1
				new_review = Reviews(review_number, username, isbn, review_title, review_text, review_rating)
				db.add(new_review)
				db.commit()
				return {'message': "Review submitted"}
		else:
			db.query(Reviews).filter_by(
				  username=username, isbn=isbn).update({
						'review_text': review_text,
						'review_title': review_title,
						'review_rating': review_rating
					})
			db.commit()
			return {'message': "Review updated"}

def get_review(database, Reviews, isbn=0, username=''):
	if username == '':
		review = database.query(Reviews).filter_by(isbn=isbn).all()
	else:
		review = database.query(Reviews).filter_by(username=username, isbn=isbn).all()
	return review