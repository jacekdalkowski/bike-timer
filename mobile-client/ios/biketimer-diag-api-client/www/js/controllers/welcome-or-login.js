angular.module('bikeTimerApp')
.controller('welcomeOrLoginCtrl', ['$scope', '$ionicModal', '$timeout', '$state', 
	'appStateFactory', 'facebookAccountFactory', 'bikeTimerAccountFactory', 
    function($scope, $ionicModal, $timeout, $state, appStateService, facebookAccountService, bikeTimerAccountService) {

      $scope.model = {
      	isLoggedIntoBikeTimer: identityService.getIsLoggedIntoBikeTimer()
      };

      $scope.events = {
      	logIntoBikeTimerViaFacebook: function(){
      		facebookService.getLoginStatus(function (response) {
            	bikeTimerGlobals.log('getLoginStatus, response.status === ' + response.status);
            	if (response.status !== 'connected') {
              		facebookService.login(function(facebookLoginSuccessData){
              			debugger;
              		}, 
              		function(facebookLoginFailureData){
              			debugger;
              		});
            	}
          	});
      	}
      };

}]);