var Review = (function(){
	function modifyReview(event) {
		event.preventDefault();
		var message = $("#message");
		if ($('#reviewTitle') === '' || $('#reviewText') === '' || ($('input[type=radio]:checked').length === 0)) {
			message.empty();
			message.append('Please complete all fields');
			return
		};
		data = $("#reviewForm").serialize()
		$.post("/review", data, response => {
			message.empty()
			if (response.message) {
				message.append(response.message);
			} else message.append(response.error); 	
		});
	};
	function deleteReview(event) {
		var message = $("#message")
		event.preventDefault();
		$.ajax({
			url: '/review',
			type: 'DELETE',
			success: response => {
				message.empty();
				if (response.message) {
					message.append(response.message);
				} else message.append(response.error);
			}
	 });
	};
	return {
		modify: modifyReview,
		remove: deleteReview
	}
}());

$(document).ready(function() { 
	$("#reviewSubmitButton").click(function(event) {
		Review.modify(event);
	});
	$("#reviewDeleteButton").click(function(event) {
		Review.remove(event);
	});
});
