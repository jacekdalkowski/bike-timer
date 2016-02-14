angular.module('bikeTimerApp')
.config(function($stateProvider, $urlRouterProvider, $translateProvider) {

  (function setupRoutes(){
    $stateProvider
      .state('welcome-or-login', {
        url: '/welcome-or-login',
        templateUrl: 'templates/welcome-or-login.html',
        controller: 'welcomeOrLoginCtrl'
      })
      .state('tabs', {
        url: '/tabs',
        abstract: true,
        data: {
          requireLogin: true
        },
        templateUrl: 'templates/master-view-with-side-menu.html',
        controller: 'masterViewWithSideMenuCtrl'
      })
      .state('tabs.timer', {
        url: '/timer',
        views: {
          'timer-tab': {
            templateUrl: 'templates/timer/timer.html',
            controller: 'timerCtrl'
          }
        }
      })
      .state('tabs.standings', {
        url: '/standings',
        views: {
          'standings-tab': {
            templateUrl: 'templates/standings/standings.html',
            controller: 'standingsCtrl'
          }
        }
      });
    // if none of the above states are matched, use this as the fallback
    // $urlRouterProvider.otherwise('/welcome-or-login');
    $urlRouterProvider.otherwise('/tabs/timer');
  })();

});