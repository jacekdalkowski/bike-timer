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

});