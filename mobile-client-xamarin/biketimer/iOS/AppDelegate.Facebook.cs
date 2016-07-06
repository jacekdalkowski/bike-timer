using System.Linq;
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
			var finishedLaunching = FacebookCoreKit.ApplicationDelegate.SharedInstance.FinishedLaunching(application, launchOptions);

			FacebookCoreKit.AccessToken accessToken = FacebookCoreKit.AccessToken.CurrentAccessToken;
			if (accessToken != null)
			{
				FacebookAccess facebookAccess = new FacebookAccess(
					accessToken.TokenString,
					accessToken.Permissions.Select(p => p.Self.ToString()));
				FacebookStateManager.Instance.SetAccessToken(facebookAccess);
			}

			return finishedLaunching;
		}
	}
}

