module.exports = (function() {
	
	function setupRequestCallbacks(req, res, handler){
    
		var requestBody = '';
		
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
	}
	
	return {
		setupRequestCallbacks: setupRequestCallbacks
	};
	
})();