var http = require('http');
var querystring = require('querystring');
var jwt = require('jwt-simple');
var tokenSecret = '1234567890';

http.createServer(function (req, res) {
	console.log('Got request.');
	isTokenRequestValid(req,
		function onValid(username){
			var payload, token;
			payload = {
				username: username
			};
			token = jwt.encode(payload, tokenSecret);
			res.writeHead(200, {'Content-Type': 'application/json'});
			res.end('{"token": "' + token +'"}');
			console.log('Sent response for valid credentials.');
		},
		function onInvalid(){
			res.writeHead(400);
			res.end();
			console.log('Sent response for invalid credentials.');
		});	
})
.listen(8081, '127.0.0.1');
console.log('Server running at http://127.0.0.1:8081/.');

function isTokenRequestValid(req, onValid, onInvalid){
	
	var requestBody = '';
	var isValid = true;
	
	if(req.method !== 'POST'){ isValid = false; }
	if(req.url !== '/token'){ isValid = false; }
	
    req.on('data', function(chunk) {
   		requestBody += chunk.toString();
    });
    
    req.on('end', function() {
		
		var decodedBody = querystring.parse(requestBody);
		
		if(!decodedBody.grant_type || decodedBody.grant_type !== 'password') { isValid = false; }
		//if(!decodedBody.username || decodedBody.username !== 'jacek') { isValid = false; }
		if(!decodedBody.password || decodedBody.password !== 'pass') { isValid = false; }
		
		console.log('Token request is valid: ' + isValid);
		if(isValid){
			onValid(decodedBody.username);
		}else{
			onInvalid();
		}
    });
}