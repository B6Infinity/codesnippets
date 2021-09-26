let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value; // Add `{% csrf_token %}` in your HTML somewhere above this line of code
let form = new FormData(); // Add Data to be sent to this 'form'

fetch(`serverendpoint`,
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

      // Work with the data sent by the server here

  });
