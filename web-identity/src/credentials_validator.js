module.exports = (function() {

    var facebookFacade = require('./facebook_facade');

    function validateCredentials(credentials, onValidateCredentialsSuccess, onValidateCredentialsError) {
        if(credentials.grantType === 'facebook_token'){
            facebookFacade.getUserProfile(credentials.accessToken,
                function onGetUserProfileSuccess(fbResponse){
                    onValidateCredentialsSuccess({
                        email: fbResponse.email,
                        fbId: fbResponse.id,
                        fbName: fbResponse.first_name,
                        fbSurname: fbResponse.last_name,
                        fbAccessToken: credentials.accessToken
                    });
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