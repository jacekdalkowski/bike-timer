angular.module('bikeTimerApp')

.controller('masterViewWithSideMenuCtrl', ['$scope', '$ionicModal', '$timeout', 'facebookService',
    function($scope, $ionicModal, $timeout, facebookService) {

      $scope.events = {

        fbLogin: function () {
          facebookService.getLoginStatus(function (response) {
            btGlobals.log('getLoginStatus, response.status === ' + response.status);
            if (response.status !== 'connected') {
              facebookService.login(function(){}, function(){});
            }
          });
        },

        fbLogout: function () {
          facebookService.logout(
            function onSuccess(){
              btGlobals.log('Successfull logout');
            },
            function onFailure(){
              btGlobals.log('Unsuccessfull logout');
            });
        }

      };

}]);