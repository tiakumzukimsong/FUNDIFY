function validateForm() {
	var email = document.forms["signupForm"]["email"].value;
	var password = document.forms["signupForm"]["password"].value;
	var confirmPassword = document.forms["signupForm"]["confirm-password"].value;

	if (!isValidEmail(email)) {
		alert("Please enter a valid email address");
		return false;
	}

	if (!isValidPassword(password)) {
		alert("Please enter a password that meets the following requirements:\n- At least 8 characters long\n- Contains at least one uppercase letter, one lowercase letter, and one number");
		return false;
	}

	if (password != confirmPassword) {
		alert("Passwords do not match");
		return false;
	}
}

function isValidEmail(email) {
	// Regular expression pattern for email validation
	var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	return emailPattern.test(email);
}

function isValidPassword(password) {
	// Regular expression patterns for password validation
	var lengthPattern = /.{8,}/;
	var uppercasePattern = /[A-Z]/;
	var lowercasePattern = /[a-z]/;
	var numberPattern = /\d/;
	return lengthPattern.test(password) &&
