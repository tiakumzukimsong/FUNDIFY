function validateForm() {
    var email = document.forms["loginForm"]["email"].value;
    var password = document.forms["loginForm"]["password"].value;

    if (email == "") {
        alert("Email must be filled out");
        return false;
    }

    if (password == "") {
        alert("Password must be filled out");
        return false;
    }
}
