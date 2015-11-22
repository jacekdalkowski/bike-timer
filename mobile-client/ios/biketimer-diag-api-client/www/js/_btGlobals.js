
var btGlobals = null;

(function(){

	var envs = {
		localBrowser: "LOCAL_BROWSER",
		mobileDiag: "MOBILE_DIAG",
		mobileClientProd: "MOBILE_CLIENT_PROD"
	};

	btGlobals = {
		envs: envs,
		currentEnv: envs.localBrowser,
		fbAppId: '942813139123420',
		log: function(msg){
			alert(msg);
		}
	};

})();