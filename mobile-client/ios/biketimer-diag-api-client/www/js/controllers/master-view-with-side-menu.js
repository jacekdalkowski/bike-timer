angular.module('bikeTimerApp')
.controller('masterViewWithSideMenuCtrl', ['$scope', '$ionicModal', '$timeout', '$state', 'facebookService',
    function($scope, $ionicModal, $timeout, $state, facebookService) {

      $scope.masterModel = {
        navState: $state
      };

      $scope.masterEvents = {

        fbLogin: function () {
          facebookService.getLoginStatus(function (response) {
            bikeTimerGlobals.log('getLoginStatus, response.status === ' + response.status);
            if (response.status !== 'connected') {
              facebookService.login(function(){}, function(){});
            }
          });
        },

        fbLogout: function () {
          facebookService.logout(
            function onSuccess(){
              bikeTimerGlobals.log('Successfull logout');
            },
            function onFailure(){
              bikeTimerGlobals.log('Unsuccessfull logout');
            });
        }

      };

}]);