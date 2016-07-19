using System.Linq;
using Foundation;
using UIKit;
using FacebookCoreKit = global::Facebook.CoreKit;

namespace Biketimer.iOS
{
	public partial class AppDelegate
	{
		private bool FacebookSetupOnFinishedLaunching(NSDictionary launchOptions)
		{
			//FacebookCoreKit.Settings.AppID = "258884457813694";
			//FacebookCoreKit.Settings.DisplayName = "biketimer";

			AccountManager.Instance.LoginCompleted += OnLoginCompleted;

			// This method verifies if you have been logged into the app before, and keep you logged in after you reopen or kill your app.
			var finishedLaunching = FacebookCoreKit.ApplicationDelegate.SharedInstance.FinishedLaunching(_iOSApp, launchOptions);

			FacebookCoreKit.AccessToken accessToken = FacebookCoreKit.AccessToken.CurrentAccessToken;
			if (accessToken != null)
			{
				FacebookAccess facebookAccess = new FacebookAccess(
					accessToken.TokenString,
					accessToken.Permissions.Select(p => p.Self.ToString()));
				//FacebookStateManager.Instance.SetAccessToken(facebookAccess);
				Account accountData = GetAccountData();
				if (accountData != null)
				{
					AccountManager.Instance.RestoreAccountData(accountData);
				}
			}

			return finishedLaunching;
		}

		private void OnLoginCompleted(Account accountData)
		{
			SaveAccountData(accountData);
		}
	}
}

