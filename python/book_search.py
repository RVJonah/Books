def book_search(database, Books, search_term, search_type):
	matching_books = False
	if search_type == 'ISBN':
		matching_books = database.query(Books).filter(Books.isbn.ilike('%%{}%%'.format(search_term))).all()
	if search_type == 'Book Title':
		matching_books = database.query(Books).filter(Books.title.ilike('%%{}%%'.format(search_term))).all()
	if search_type == 'Author':
		matching_books = database.query(Books).filter(Books.author.ilike('%%{}%%'.format(search_term))).all()
	if matching_books == False or matching_books == []:
		return False
	return matching_books
