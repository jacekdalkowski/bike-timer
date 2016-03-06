module.exports = (function() {
	
	var querystring = require('querystring');
	var credentialsValidator = require('./credentials_validator');
	var btUserService = require('./biketimer_user_service');
	var jwt = require('jwt-simple');
	
	var tokenSecret = '1234567890';
	
	function handleTokenRequest(req, res, requestBody){
		var decodedBody = querystring.parse(requestBody);
		credentialsValidator.validate(decodedBody,
			function onSuccess(userData){
				btUserService.getOrAddUser(userData,
					function onSuccess(userBtEntity){
						var currentDate = new Date();
						var twoWeeksAheadDate = new Date();
						twoWeeksAheadDate.setDate(currentDate.getDate()+14)
						var tokenPayload = {
							nbf: '0',
							exp: twoWeeksAheadDate.getTime(),
							iat: '0',
							btUserId: userBtEntity.id 
						};
						var token = jwt.encode(tokenPayload, tokenSecret);
						res.writeHead(200, {'Content-Type': 'application/json'});
						res.end('{"token": "' + token + '"}');
						console.log('Sent response for valid credentials.');
					},
					createErrorHandler(req, res));
			},
			createErrorHandler(req, res));
	}
	
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
	
	return {
        handleTokenRequest: handleTokenRequest
    };
	
})();