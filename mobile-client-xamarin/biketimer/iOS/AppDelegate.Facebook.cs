using Foundation;
using UIKit;
using FacebookCoreKit = global::Facebook.CoreKit;

namespace Biketimer.iOS
{
	public partial class AppDelegate
	{
		private bool FacebookSetupOnFinishedLaunching(UIApplication application, NSDictionary launchOptions)
		{
			//FacebookCoreKit.Settings.AppID = "258884457813694";
			//FacebookCoreKit.Settings.DisplayName = "biketimer";

			// This method verifies if you have been logged into the app before, and keep you logged in after you reopen or kill your app.
			return FacebookCoreKit.ApplicationDelegate.SharedInstance.FinishedLaunching(application, launchOptions);
		}
	}
}

