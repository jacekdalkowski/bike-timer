module.exports = (function() {
	
	var tokenRequestHandler = require('./token_request_handler');
	
	function mapHandler(req, res){
		if(req.method === 'POST' && req.url === '/token'){ 
			return tokenRequestHandler.handleTokenRequest;
		}else{
			res.writeHead(404);
			res.end();
		}
	}
	
	return {
		mapHandler: mapHandler
	};
	
})();