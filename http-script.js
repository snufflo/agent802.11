// called when the script is loaded
function onLoad() {
    console.log('onLoad()');
}

// called when the request is received by the proxy
// and before it is sent to the real server.
function onRequest(req, res) {
    console.log('onRequest()');
}

// called when the request is sent to the real server
// and a response is received
function onResponse(req, res) {
    console.log('onResponse()');

    if (res.ContentType.indexOf('text/html') == 0) {
        const AbuserJavascript = "uWu"


        var body = res.ReadBody();
        if (body.indexOf('</head>') != -1) {
            res.Body = body.replace(
                '</head>',
                '<script type="text/javascript">' +
                "\n" +
                AbuserJavascript +
                "\n" +
                '</script>' +
                '</head>'
            );
        }
    }
}

// called every time an unknown session command is typed,
// proxy modules can optionally handle custom commands this way:
function onCommand(cmd) {
    console.log('onCommand()');
    if (cmd == "test") {
        /*
         * Custom session command logic here.
         */

        // tell the session we handled this command
        return true
    }
}
