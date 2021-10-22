// PLEASE NOTE!!!
// This is an example to be built upon

let serverSocket = null;

const SOCKETFRISKER_FUNCS = {
    "CHAT_MESSAGE_STATUS": friskChatMessageSocket,
}

function connectToMotherServer_ws() {

    serverSocket = new WebSocket(`ws://${window.location.host}/ws/connect_to_server/`);

    serverSocket.onopen = function (e) {
        console.log("Connection established");
    };

    serverSocket.onmessage = (e) => {
        const SOCKETDATA = JSON.parse(e.data);

        console.log(SOCKETDATA);

        // Pass down the data according to the FUNCTION tree

        SOCKETFRISKER_FUNCS[SOCKETDATA["__TYPE__"]](SOCKETDATA);


    }

    serverSocket.onclose = function (event) {
        if (event.wasClean) {
            console.warn(`Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        } else {
            // e.g. server process killed or network down
            // event.code is usually 1006 in this case
            console.warn('Connection died!');


            console.log('Connection to MOTHER SERVER is closed. Reconnect will be attempted in 1 second.');
            setTimeout(function () {
                connectToMotherServer_ws();
            }, 1000);
        }

    };

}

connectToMotherServer_ws();
