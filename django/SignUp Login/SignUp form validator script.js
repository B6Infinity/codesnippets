
// Frisk Form

let ERRORS = 0;


// Username Exists |!

let form = new FormData();
form.append('username_to_check_availability', document.getElementById('signup_username').value);

fetch(`usernameexists`,
    {
        method: 'POST',
        body: form,
        headers: {
            'Accept': 'multipart/form-data, application/json, text/plain, */*',
            "X-CSRFToken": csrftoken
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data["SUCCESS"]) {
            // NICE Then
        } else {
            for (let error in data["ERRORS"]) {
                createAlertMessage('error', data["ERRORS"][error]);
                ERRORS++;
            }
        }
    });

// If Passwords Match
if (document.getElementById('signup_password').value != document.getElementById('cf_signup_password').value) {
    createAlertMessage('error', "Passwords don't match"); ERRORS++;
}

console.log(document.getElementById('agreed2TNC').value);
if (document.getElementById('agreed2TNC').value != 'on') {
    ERRORS++; createAlertMessage('error', "You must agree to the <a href='#'>Terms and Conditions</a>");
}

removeLoaderUI(document.getElementById('signup_btn'), "SIGN UP");

if (ERRORS == 0){
    signupform.submit();
}
