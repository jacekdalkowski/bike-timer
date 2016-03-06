var http = require('http');
var requestToHandlerMapper = require('./request_to_handler_mapper.js');
var requestUtils = require('./request_utils.js');

http.createServer(function (req, res) {
    
    console.log('\nGot request, method: ' + req.method + ', url: ' + req.url);
    
	var handler = requestToHandlerMapper.mapHandler(req, res);
    requestUtils.setupRequestCallbacks(req, res, handler);

})
.listen(8081);

console.log('Server running at http://127.0.0.1:8081/.');








