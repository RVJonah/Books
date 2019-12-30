var Login = (function () {
	function login(event) {
			event.preventDefault();
			var data = $('#registrationForm').serialize();
			var data = data + "&check=" + true;
			var msg = "";
			var fields = $("input");
			var [username, pass, confpass, email, confemail] = fields;
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
			if (pass.value !== confpass.value) {
				message.empty();
				message.append("Passwords need to match");
				return false;
			}
			if (email.value !== confemail.value) {
				message.empty();
				message.append("Email addresses must match");
				return false;
			}
			$.post("/register", data, function (response) {
				console.log(response)
				if (response === true ) {
					$("#registrationForm").submit();
				} else {
					message.empty();
					message.append(response.error);
				}
			});
	}
	return login;
}());

$(document).ready(function () {
	$("#registerButton").click(function (event) {
			Login(event);
	});
});