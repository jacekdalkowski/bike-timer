module.exports = (function() {

    var https = require('https');
    
    function getUserProfile(fbAccessToken, onGetUserProfileSuccess, onGetUserProfileError) {
        
        var fbRequestOptions = {
            host: 'graph.facebook.com',
            port: 443,
            path: '/me?fields=id,email,first_name,last_name&access_token=' + fbAccessToken,
            method: 'GET'
        };

        var fbResponseHandler = function(fbResponse) {
            var responseRaw = '';

            fbResponse.on('data', function (chunk) {
                responseRaw += chunk;
            });

            fbResponse.on('end', function (a,b,c,d) {
                var responseObject = JSON.parse(responseRaw);
                if(this.statusCode === 200){
                    onGetUserProfileSuccess(responseObject);
                }else{
                    if(responseObject.error && responseObject.error.message){
                        onGetUserProfileError('bad_request', 'Facebook error: ' + responseObject.error.message);
                    }else{
                        onGetUserProfileError('external_system_error', 'Unknown facebook error occured. Facebook response code: ' + this.statusCode);
                    }
                }
            });
        };

        https.request(fbRequestOptions, fbResponseHandler).end();
    };
    
    return {
        getUserProfile: getUserProfile
    };

}());