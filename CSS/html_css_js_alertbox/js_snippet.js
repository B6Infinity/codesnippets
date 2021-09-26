
    
        function closeAlertMessage(alertBoxCLSBTN) {

            alertBoxCLSBTN.parentElement.classList.add("exitAlert");
            setTimeout(function () { alertBoxCLSBTN.parentElement.remove(); }, 600);
        }

        function closeAlertMessage_TO(alertBox) {

            alertBox.classList.add("exitAlert");
            setTimeout(function () { alertBox.remove(); }, 600);
        }

        function createAlertMessage(tag, message) {
            let alertBoxContainer = document.getElementById('alert-box-container');

            let symbol = ``;
            if (tag == 'warning') {
                symbol = '<span class="alert-icon fas fa-exclamation"></span>';
            } else if (tag == 'info') {
                symbol = '<span class="alert-icon fas fa-info" ></span>';

            } else if (tag == 'success') {
                symbol = '<span class="alert-icon fas fa-check" ></span>';

            } else if (tag == 'error') {
                symbol = '<span class="alert-icon fas fa-times"></span>';

            }


            var current = new Date();

            let alertuid = String(current.getHours()) + String(current.getMinutes()) + String(current.getSeconds()) + String(current.getMilliseconds());

            alertBoxContainer.innerHTML += `
                <div class="alert-box ${tag} enterAlert" id="${alertuid}">
                    ${symbol}
                    <span class="alert-message">${message}
                    </span>
                    <span class="alert-closebtn fas fa-times" onclick="closeAlertMessage(this)"></span>
                </div>
                `;

            setTimeout(function () { document.getElementsByClassName('enterAlert')[0].classList.remove('enterAlert'); }, 200);
            setTimeout(function () {
                closeAlertMessage_TO(document.getElementById(alertuid));
            }, 6000); // Delete Alert after 6 seconds

        }


    
