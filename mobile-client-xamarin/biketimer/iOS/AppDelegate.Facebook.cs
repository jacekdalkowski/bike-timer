using System.Linq;
using Foundation;
using UIKit;
using FacebookCoreKit = global::Facebook.CoreKit;
using Biketimer.Account;

namespace Biketimer.iOS
{
	public partial class AppDelegate
	{
		private bool FacebookSetupOnFinishedLaunching(NSDictionary launchOptions)
		{
			//FacebookCoreKit.Settings.AppID = "258884457813694";
			//FacebookCoreKit.Settings.DisplayName = "biketimer";

			AccountManager.Instance.LoginCompleted += OnLoginCompleted;

			AccountData accountData = GetAccountData();
			if (accountData != null)
			{
				// This method verifies if you have been logged into the app before, and keep you logged in after you reopen or kill your app.
				var finishedLaunching = FacebookCoreKit.ApplicationDelegate.SharedInstance.FinishedLaunching(_iOSApp, launchOptions);

				FacebookCoreKit.AccessToken accessToken = FacebookCoreKit.AccessToken.CurrentAccessToken;
				if (accessToken != null)
				{
					AccountManager.Instance.RestoreAccountData(accountData);
					return finishedLaunching;
				}
			}

			return true;
		}

		private void OnLoginCompleted(AccountData accountData)
		{
			SaveAccountData(accountData);
		}
	}
}

