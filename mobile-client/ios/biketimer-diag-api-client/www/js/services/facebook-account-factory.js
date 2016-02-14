angular.module('bikeTimerApp.services')
.factory('facebookAccountFactory', ['$http', 'apiUrl', function($http, apiUrl){

	return {
		getLoginStatus: function(onResponse){
			facebookConnectPlugin.getLoginStatus(function (response) {
				onResponse(response);
			});
		},
		login: function(onSuccess, onFailure){
			facebookConnectPlugin.login(['email', 'public_profile'], onSuccess, onFailure);
		},
		logout: function(onSuccess, onFailure){
			facebookConnectPlugin.logout(onSuccess, onFailure);
		}
	};
	
}]);