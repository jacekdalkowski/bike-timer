var http = require('http');
var querystring = require('querystring');
var jwt = require('jwt-simple');
var credentialsValidator = require('./credentials_validator');
var btUserService = require('./biketimer_user_service');
var tokenSecret = '1234567890';

http.createServer(function (req, res) {
    
    console.log('\nGot request, method: ' + req.method + ', url: ' + req.url);
    
    var requestBody = '';
	var handler = mapHandler(req, res);

    req.on('data', function(chunk) {
        if(handler){
            requestBody += chunk.toString();   
        }
    });
    
    req.on('end', function(){
        if(handler){
            handler(req, res, requestBody); 
        }
    });

})
.listen(8081);
console.log('Server running at http://127.0.0.1:8081/.');

function mapHandler(req, res){
    if(req.method === 'POST' && req.url === '/token'){ 
        return tokenRequestHandler;
    }else{
        res.writeHead(404);
        res.end();
    }
}

function tokenRequestHandler(req, res, requestBody){
    var decodedBody = querystring.parse(requestBody);
    credentialsValidator.validate(decodedBody,
        function onSuccess(userData){
            btUserService.getOrAddUser(userData,
                function onSuccess(userBtEntity){
                    var currentDate = new Date();
                    var twoWeeksAheadDate = new Date();
                    twoWeeksAheadDate.setDate(twoWeeksAheadDate.getDate()+14)
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
