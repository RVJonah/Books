'use strict';
var Login = (function () {
	function login(event) {
		event.preventDefault();
			var data = $('#loginform').serialize();
			var data = data + "&check=" + true;
			var msg = "";
			var fields = $("input");
			var message = $("#message");
			$.each(fields, function () {
					if (this.value === "") {
							msg += this.title + ' is required.<br>';
					}
			});
			if (msg) {
					message.empty();
					message.append(msg);
					return false;
			}
			$.post("/login", data, function (response) {
				if (response === true ) {
					$("#loginform").submit();
				} else {
					message.empty();
					message.append(response.error);
				}
			});
	}
	return login;
}());

$(document).ready(function () {
	$("#loginButton").click(function (event) {
			Login(event);
	});
});