module.exports = (function() {

    var facebookFacade = require('./facebook_facade');

    function validateCredentials(credentials, onValidateCredentialsSuccess, onValidateCredentialsError) {
        if(credentials.grantType === 'facebook_token'){
            facebookFacade.getUserProfile(credentials.accessToken,
                function onGetUserProfileSuccess(fbResponse){
                    onValidateCredentialsSuccess(fbResponse);
                },
                onValidateCredentialsError);
        }else{
            onValidateCredentialsError('bad_request', 'Unsupported grant type.');
        }
    };
    
    return {
        validate: validateCredentials
    };

}());