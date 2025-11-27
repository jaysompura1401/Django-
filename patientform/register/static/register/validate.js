function validateForm() {
    let name = document.getElementById("name").value.trim();
    let age = document.getElementById("age").value.trim();
    let email = document.getElementById("email").value.trim();
    let phone = document.getElementById("phone").value.trim();
    let disease = document.getElementById("disease").value.trim();
    let errorMessage = document.getElementById("error-message");

    errorMessage.textContent = "";

    if (name === "" || age === "" || email === "" || phone === "" || disease === "") {
        errorMessage.textContent = "All fields are required!";
        return false;
    }

    if (isNaN(age) || age <= 0) {
        errorMessage.textContent = "Please enter a valid age.";
        return false;
    }

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!emailPattern.test(email)) {
        errorMessage.textContent = "Please enter a valid email address.";
        return false;
    }

    const phonePattern = /^[0-9]{10}$/;
    if (!phonePattern.test(phone)) {
        errorMessage.textContent = "Phone number must be 10 digits.";
        return false;
    }

    alert("Registration Successful!");
    return true;
}
