const http = require('http');
const os = require('os');
console.log("http server starting...");
var handler = function(request, response) {
	console.log("Received request from " + request.connection.remoteAddress);
	response.writeHead(200);
	response.end("you have hit " + os.hostname() + "\n");
};
var www = http.createServer(handler);
www.listen(8080);
