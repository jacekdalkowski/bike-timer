angular.module('bikeTimerApp.services')
.factory('bikeTimerAccountFactory', ['$http', 'apiUrl', 'identityUrl', function($http, apiUrl, identityUrl){

	var _isLoggedIntoBikeTimer = false;
	var _bikeTimerToken;

	function getLoginStatus(){
		return _isLoggedIntoBikeTimer;
	}

	function loginViaFbToken(){

	}

	function setIsLoggedOut(){
		_isLoggedIntoBikeTimer = false;
	}

	return {
		getLoginStatus: getLoginStatus,
		loginViaFbToken: loginViaFbToken,
		setIsLoggedOut: setIsLoggedOut
	};

}]);