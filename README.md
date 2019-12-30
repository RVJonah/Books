# Project 1

Web Programming with Python and JavaScript


Books

Books is a book review service which uses GoodReads API alongside it's own user reviews to provide ratings and written reviews.
The site can be used via the login and registration pages which give access to the search page. Once a user has searched for a book either via ISBN, author or book title, the book can be selected which the provides more detailed information and any past reviews from other users on the selected book. The user is also free to write a review of their own or is able to update the review they have written should they decide to.

The final function of this app is the API service. This uses the /API/<ISBN> route where ISBN is the isbn of the requested book. This returns a JSON object in the following format:
  
 {
    "title": "",
    "author": "",
    "year": "",
    "isbn": "",
    "review_count": "",
    "average_score": ""
  }

  In order to run this service clone the directory and install the required modules found in the requirments.txt.
  Then set the follow environment variables:
  FLASK_APP='application.py'
  DATABASE_URI= your database uri
  GOODREADS_KEY= your goodreads api key

