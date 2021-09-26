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
        if(data["SUCCESS"]){
            // Success HTML
        }else{
            for(let error in data["ERRORS"])
            // Manipulate the error text --(verbosity text)
        }

        // Work with the data sent by the server here

    });
