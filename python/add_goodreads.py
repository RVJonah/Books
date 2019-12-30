import os
import requests
def add_goodreads_data(books_data, isbn):
	goodreads_data = requests.get("https://www.goodreads.com/book/review_counts.json",
  params={"key": os.environ['GOODREADS_KEY'],
  "isbns": isbn}).json()
	books_data["average_score"] = goodreads_data["books"][0]["average_rating"]
	books_data["review_count"] = goodreads_data["books"][0]["work_ratings_count"]
	return books_data
