angular.module('bikeTimerApp')
.config(function($stateProvider, $urlRouterProvider, $translateProvider) {

  (function setupTranslations(){
    $translateProvider
      .useStaticFilesLoader({
        prefix: 'js/translations/',
        suffix: '.json'
      })
      .registerAvailableLanguageKeys(['en', 'pl'], {
        'en' : 'en', 'en_GB': 'en', 'en_US': 'en',
        'pl' : 'pl', 'pl_PL': 'pl'
      })
      .preferredLanguage('en')
      .fallbackLanguage('en')
      .determinePreferredLanguage()
      .useSanitizeValueStrategy('escapeParameters');
  })();

  (function setupRoutes(){
    $stateProvider
      .state('tabs', {
        url: '/tabs',
        abstract: true,
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
    $urlRouterProvider.otherwise('/tabs/timer');
  })();

});