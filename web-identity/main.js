var http = require('http');
var querystring = require('querystring');
var jwt = require('jwt-simple');
var credentialsValidator = require('./credentials_validator');
var btUserService = require('./biketimer_user_service');
var tokenSecret = '1234567890';

http.createServer(function (req, res) {
    var requestBody = '';
	var isValid = true;
	console.log('\nGot request.');
	
	if(req.method !== 'POST'){ isValid = false; }
	if(req.url !== '/token'){ isValid = false; }
	
    req.on('data', function(chunk) {
   		requestBody += chunk.toString();
    });
    
    req.on('end', function() {
		var decodedBody = querystring.parse(requestBody);
        credentialsValidator.validate(decodedBody,
            function onSuccess(userIdInfo){
                btUserService.getOrAddUser(userIdInfo,
                    function onSuccess(userBtEntity){
                        var tokenPayload = {
                            btUserId: userBtEntity.Id 
                        };
                        var token = jwt.encode(tokenPayload, tokenSecret);
                        res.writeHead(200, {'Content-Type': 'application/json'});
                        res.end('{"token": "' + token + '"}');
                        console.log('Sent response for valid credentials.');
                    },
                    createErrorHandler(req, res));
            },
            createErrorHandler(req, res));
        
        //facebookFacade.getUserProfile('CAACEdEose0cBABTwb9WaLbxHYv6kvt0qeOZANHwYYfv1DUo5TLZB2QZAKxexZBvxWZAzEQTZCbX6AU79x9klNDyNZApCvHhbQO7UsLPp6mOsydYRyG03zb6UjBmXZCUJAyp9ZC9ZCxsPAwWhc5956KKgB3ysKvoZCIFs6OA1QXaXS4oyp0xCgwxulvzAqCB7YGdIU3BogeBT4AbdAZDZD');
    });
    
    
    /*credentialsValidator.validate()
	isTokenRequestValid(req,
		function onValid(username){
			var payload, token;
			payload = {
				btUserId: '123321'
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
		});	*/
})
.listen(8081, '127.0.0.1');
console.log('Server running at http://127.0.0.1:8081/.');

function createErrorHandler(req, res){
    return function(type, msg){
        if(type === 'invalid_credentials' || type === 'bad_request'){
            res.writeHead(400);
        }else{
            res.writeHead(500);
        }
        res.end('{"error": "' + msg + '"}');
        console.log('Sent response for invalid credentials.');
    };
}

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
		
        facebookFacade.getUserProfile('CAACEdEose0cBABTwb9WaLbxHYv6kvt0qeOZANHwYYfv1DUo5TLZB2QZAKxexZBvxWZAzEQTZCbX6AU79x9klNDyNZApCvHhbQO7UsLPp6mOsydYRyG03zb6UjBmXZCUJAyp9ZC9ZCxsPAwWhc5956KKgB3ysKvoZCIFs6OA1QXaXS4oyp0xCgwxulvzAqCB7YGdIU3BogeBT4AbdAZDZD');
        
		console.log('Token request is valid: ' + isValid);
		if(isValid){
			onValid(decodedBody.username);
		}else{
			onInvalid();
		}
    });
}