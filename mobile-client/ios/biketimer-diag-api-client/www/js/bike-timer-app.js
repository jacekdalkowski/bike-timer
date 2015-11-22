// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.controllers' is found in controllers.js
angular.module('bikeTimerApp', ['ionic', 'bikeTimerApp.services'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {

    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);

    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})

.config(function($stateProvider, $urlRouterProvider) {

  function configureFbForBrowser(){
    alert("Configuring FB for web browser");
    var appID = 942813139123420;
    var version = "v2.5"; // or leave blank and default is v2.0
    //$cordovaFacebookProvider.browserInit(appID, version);
  }

  if(!window.cordova){
    configureFbForBrowser();
  }

  $stateProvider
    .state('app', {
      url: '/app',
      abstract: true,
      templateUrl: 'templates/master-view-with-side-menu.html',
      controller: 'masterViewWithSideMenuCtrl'
    })
    .state('app.welcome', {
      url: '/welcome',
      views: {
        'mainContent': {
          templateUrl: 'templates/welcome.html'//,
          //controller: 'welcomeCtrl'
        }
      }
    });

  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/app/welcome');
});
