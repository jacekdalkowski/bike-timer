angular.module('bikeTimerApp')

.controller('masterViewWithSideMenuCtrl', function($scope, $ionicModal, $timeout, ngFB) {

  $scope.fbLogin = function () {
    ngFB.login({scope: 'public_profile,user_friends,email'}).then(
      function (response) {
        if (response.status === 'connected') {
            console.log('Facebook login succeeded');
        } else {
            alert('Facebook login failed');
        }
      });
  };

});