const Search = (function(){
		function search(event) { 
			const searchResultsBox = $('#searchResults');
			event.preventDefault();
			let searchData = $('#searchForm').serialize();
			if ($('#searchText').val() === '') {
				searchResultsBox.append('Please enter a search value');
				return
			}
			$.post('/search', searchData, response => {
				searchResultsBox.empty();
				if (response.error) {
					searchResultsBox.append(response.error);
					return
				}
				searchResultsBox.append( 
					`<table>
						<thead>
							<tr>
								<th>ISBN</th>
								<th>Book Title</th>
								<th>Author</th>
							</tr>
							</thead>
							<tbody>
							</tbody>
							<table>`
				);
				response.forEach(book => {
					$('#searchResults table tbody').append(
					`<tr>
					<td><a href="/book?isbn=${book['isbn']}">${book['isbn']}</a></td>
					<td>${book['title']}</td>
					<td>${book['author']}</td>
					</tr>`
					); 
				});
			});
		};
		return search
	}());

$(document).ready(function () {
	$("#searchButton").click(function(event) {
			Search(event);
	});
});