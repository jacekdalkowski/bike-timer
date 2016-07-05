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
		private FacebookLoginKit.LoginButton _loginButton;
		private FacebookCoreKit.ProfilePictureView _pictureView;

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
			FacebookStateManager.Instance.LoginCompleted += OnLoginCompleted;
			FacebookCoreKit.AccessToken accessToken = FacebookCoreKit.AccessToken.CurrentAccessToken;
			if (accessToken != null)
			{
				FacebookAccess facebookAccess = new FacebookAccess(
					accessToken.TokenString,
					accessToken.Permissions.Select(p => p.Self.ToString()));
				FacebookStateManager.Instance.SetAccessToken(facebookAccess);
			}
			
			_loginButton = CreateLoginButton();
			_pictureView = new FacebookCoreKit.ProfilePictureView(new CGRect(50, 50, 220, 220));

			if (FacebookStateManager.Instance.Account != null)
			{
				SetupViewForLoggedIn();
			}
			else
			{
				SetupViewForNotLoggedIn();
			}



			//// The user image profile is set automatically once is logged in
			//pictureView 

			//// Add views to main view
			//View.AddSubview(loginButton);
			//View.AddSubview(pictureView);
		}

		private void SetupViewForLoggedIn()
		{
			if (!View.Subviews.Any(s => s == _pictureView))
			{
				View.AddSubview(_pictureView);
			}
			if (!View.Subviews.Any(s => s == _loginButton))
			{
				View.AddSubview(_loginButton);
			}
		}

		private void SetupViewForNotLoggedIn()
		{
			if (View.Subviews.Any(s => s == _pictureView))
			{
				_pictureView.RemoveFromSuperview();
			}
			if (!View.Subviews.Any(s => s == _loginButton))
			{
				View.AddSubview(_loginButton);
			}
		}

		private FacebookLoginKit.LoginButton CreateLoginButton()
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

			return loginButton;
		}



		private void OnAccessTokenReceived(object sender, FacebookLoginKit.LoginButtonCompletedEventArgs eventArgs)
		{
			if (eventArgs.Error != null || eventArgs.Result.IsCancelled)
			{
				return;
			}

			ViewHelpers.AddLoadingOverlay(View);

			FacebookAccess facebookAccess = new FacebookAccess(
				eventArgs.Result.Token.TokenString,
				eventArgs.Result.Token.Permissions.Select(p => p.Self.ToString()));

			FacebookStateManager.Instance.SetAccessToken(facebookAccess);
		}

		/// <summary>
		/// Called when login process is completed by FacebookManager.
		/// </summary>
		private void OnLoginCompleted(FacebookAccount facebookAccountData)
		{
			InvokeOnMainThread(() =>
			{
				SetupViewForLoggedIn();
				ViewHelpers.RemoveLoadingOverlay(View);
			});
		}

		private void OnLoggedOut(object sender, EventArgs eventArgs)
		{
			FacebookStateManager.Instance.OnLoggedOut();
			InvokeOnMainThread(() =>
			{
				SetupViewForNotLoggedIn();
			});
		}

	}
}