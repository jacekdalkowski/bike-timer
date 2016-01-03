angular.module('bikeTimerApp', ['ionic', 'bikeTimerApp.services'])
.config(function($stateProvider, $urlRouterProvider) {

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