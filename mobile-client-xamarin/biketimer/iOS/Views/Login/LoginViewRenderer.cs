using System;
using System.Linq;
using CoreGraphics;
using UIKit;
using Xamarin.Forms;
using Xamarin.Forms.Platform.iOS;
using Biketimer.iOS;
using FacebookLoginKit = Facebook.LoginKit;
using FacebookCoreKit = Facebook.CoreKit;


[assembly: ExportRenderer(typeof(Biketimer.Views.Login.LoginView), typeof(Biketimer.iOS.Views.Login.LoginViewRenderer))]
namespace Biketimer.iOS.Views.Login
{
	public class LoginViewRenderer : PageRenderer
	{
		private FacebookCoreKit.ProfilePictureView pictureView;

		public override void ViewDidLoad()
		{
			//base.ViewDidLoad();

			//View.BackgroundColor = UIColor.White;
			//Title = "My Custom View Controller";

			//var btn = UIButton.FromType(UIButtonType.System);
			//btn.Frame = new CGRect(20, 200, 280, 44);
			//btn.SetTitle("Click Me", UIControlState.Normal);

			//var user = new UIViewController();
			//user.View.BackgroundColor = UIColor.Magenta;

			//btn.TouchUpInside += (sender, e) =>
			//{
			//	this.NavigationController.PushViewController(user, true);
			//};

			//View.AddSubview(btn);

			base.ViewDidLoad();

			string p = null;

			if (p == null)
			{
				RenderForLoggedIn();
			}
			else
			{
				RenderForNotLoggedIn();
			}



			//// The user image profile is set automatically once is logged in
			//pictureView = new FacebookCoreKit.ProfilePictureView(new CGRect(50, 50, 220, 220));

			//// Add views to main view
			//View.AddSubview(loginButton);
			//View.AddSubview(pictureView);
		}

		private void RenderForLoggedIn()
		{
			RenderFacebookButton();
		}

		private void RenderForNotLoggedIn()
		{
			RenderFacebookButton();
		}

		private void RenderFacebookButton()
		{
			FacebookLoginKit.LoginButton loginButton = new FacebookLoginKit.LoginButton(new CGRect(48, 0, 218, 46))
			{
				LoginBehavior = FacebookLoginKit.LoginBehavior.Native,
				ReadPermissions = new string[] { "public_profile" }
			};

			// Handle actions once the user is logged in
			loginButton.Completed += OnAccessTokenReceived;

			// Handle actions once the user is logged out
			loginButton.LoggedOut += OnLoggedOut;

			FacebookStateManager.Instance.LoginCompleted += OnLoginCompleted;

			View.AddSubview(loginButton);
		}

		private void OnAccessTokenReceived(object sender, FacebookLoginKit.LoginButtonCompletedEventArgs eventArgs)
		{
			if (eventArgs.Error != null || eventArgs.Result.IsCancelled)
			{
				return;
			}

			var bounds = UIScreen.MainScreen.Bounds;

			ViewHelpers.AddLoadingOverlay(View);

			FacebookAccess facebookAccess = new FacebookAccess(
				eventArgs.Result.Token.TokenString,
				eventArgs.Result.Token.Permissions.Select(p => p.Self.ToString()));

			System.Threading.Tasks.Task.Run(async () => await FacebookStateManager.Instance.OnAccessTokenReceived(facebookAccess));
		}

		/// <summary>
		/// Called when login process is completed by FacebookManager.
		/// </summary>
		private void OnLoginCompleted(FacebookAccount facebookAccountData)
		{
			InvokeOnMainThread(() => ViewHelpers.RemoveLoadingOverlay(View));
		}

		private void OnLoggedOut(object sender, EventArgs eventArgs)
		{
			FacebookStateManager.Instance.OnLoggedOut();
		}

		UIActivityIndicatorView spinner;
		private void showIndicator()
		{
			if (spinner == null)
			{
				spinner = new UIActivityIndicatorView(UIActivityIndicatorViewStyle.WhiteLarge);
				spinner.HidesWhenStopped = true;
				spinner.Color = UIColor.Black;
			}
			var windows = UIApplication.SharedApplication.Windows;
			Array.Reverse(windows);
			foreach (UIWindow w in windows)
			{
				if (w.WindowLevel == UIWindowLevel.Normal && !w.Hidden)
				{
					spinner.Frame = new CGRect((float)w.Bounds.GetMidX(), (float)(.66 * w.Bounds.Height), 37, 37);
					w.AddSubview(spinner);
					w.BringSubviewToFront(spinner);
					break;
				}
			}
			spinner.StartAnimating();
		}

		private void hideIndicator()
		{
			if (spinner == null)
				return;
			if (!spinner.IsAnimating)
				return;
			spinner.StopAnimating();
		}
	}
}

