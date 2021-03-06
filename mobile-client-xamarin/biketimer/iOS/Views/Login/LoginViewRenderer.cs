﻿using System;
using System.Linq;
using CoreGraphics;
using UIKit;
using Xamarin.Forms;
using Xamarin.Forms.Platform.iOS;
using Biketimer.iOS;
using FacebookLoginKit = Facebook.LoginKit;
using FacebookCoreKit = Facebook.CoreKit;
using Biketimer.Account;


[assembly: ExportRenderer(typeof(Biketimer.Views.Login.LoginView), typeof(Biketimer.iOS.Views.Login.LoginViewRenderer))]
namespace Biketimer.iOS.Views.Login
{
	public class LoginViewRenderer : PageRenderer
	{
		private FacebookLoginKit.LoginButton _loginButton;
		private FacebookCoreKit.ProfilePictureView _pictureView;
		private UILabel _welcomeLabel;

		private nfloat _pictureSide;
		private nfloat _pictureTop;

		public override void ViewDidLoad()
		{
			base.ViewDidLoad();
			AccountManager.Instance.LoginCompleted += OnLoginCompleted;
			AccountManager.Instance.LoginFailed += OnLoginFailed;

			var viewBounds = View.Bounds;
			_pictureSide = viewBounds.Width * 0.7f;
			_pictureTop = viewBounds.Height * 0.15f;

			_loginButton = CreateLoginButton();
			_pictureView = CreateProfilePicture();
			_welcomeLabel = CreateWelcomeLabel();

			if (AccountManager.Instance.AccountData != null)
			{
				SetupViewForLoggedIn();
			}
			else
			{
				SetupViewForNotLoggedIn();
			}
		}

		protected override void Dispose(bool disposing)
		{
			if (disposing)
			{
				AccountManager.Instance.LoginCompleted -= OnLoginCompleted;
				AccountManager.Instance.LoginFailed -= OnLoginFailed;
			}
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
			if (!View.Subviews.Any(s => s == _welcomeLabel))
			{
				View.AddSubview(_welcomeLabel);
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
			if (View.Subviews.Any(s => s == _welcomeLabel))
			{
				_welcomeLabel.RemoveFromSuperview();
			}
		}

		private FacebookLoginKit.LoginButton CreateLoginButton()
		{
			var viewBounds = View.Bounds;
			var buttonWidth = viewBounds.Width * 0.7f;
			var buttonHeight = viewBounds.Height * 0.08f;

			var buttonTop = viewBounds.Height * 0.035f;
			var buttonLeft = viewBounds.Width * 0.15f;

			FacebookLoginKit.LoginButton loginButton = new FacebookLoginKit.LoginButton(
					new CGRect(buttonLeft, buttonTop, buttonWidth, buttonHeight))
			{
				LoginBehavior = FacebookLoginKit.LoginBehavior.Native,
				ReadPermissions = FacebookAccess.RequiredPermissions.ToArray()
			};

			// Handle actions once the user is logged in
			loginButton.Completed += OnAccessTokenReceived;

			// Handle actions once the user is logged out
			loginButton.LoggedOut += OnLoggedOut;

			return loginButton;
		}

		private FacebookCoreKit.ProfilePictureView CreateProfilePicture()
		{
			var viewBounds = View.Bounds;
			var pictureLeft = viewBounds.Width * 0.15f;

			return new FacebookCoreKit.ProfilePictureView(new CGRect(pictureLeft, _pictureTop, _pictureSide, _pictureSide));
		}

		private UILabel CreateWelcomeLabel()
		{
			var viewBounds = View.Bounds;
			var labelWidth = viewBounds.Width * 0.7f;
			var labelHeight = viewBounds.Height * 0.08f;

			var labelTop = _pictureTop + _pictureSide + labelHeight;
			var labelLeft = viewBounds.Width * 0.15f;

			var welcomeLabel = new UILabel(new CGRect(labelLeft, labelTop, labelWidth, labelHeight));
			welcomeLabel.TextAlignment = UITextAlignment.Center;
			welcomeLabel.TextColor = UIKit.UIColor.FromRGB(59, 89, 152);
			welcomeLabel.Text = "Welcome!";

			return welcomeLabel;
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

			//FacebookStateManager.Instance.SetAccessToken(facebookAccess);
			AccountManager.Instance.StartLogin(facebookAccess);
		}

		/// <summary>
		/// Called when login process is completed by FacebookManager.
		/// </summary>
		private void OnLoginCompleted(AccountData accountData)
		{
			InvokeOnMainThread(() =>
			{
				SetupViewForLoggedIn();
				ViewHelpers.RemoveLoadingOverlay(View);
			});
		}

		private void OnLoginFailed()
		{
			InvokeOnMainThread(() =>
			{
				if (FacebookCoreKit.AccessToken.CurrentAccessToken != null)
				{
					FacebookLoginKit.LoginManager fbLoginManager = new FacebookLoginKit.LoginManager();
					fbLoginManager.LogOut();
				}

				UIAlertView error = new UIAlertView("Error", "An error occured during login", null, "Ok", null);
				error.Show();

				ViewHelpers.RemoveLoadingOverlay(View);
			});
		}

		private void OnLoggedOut(object sender, EventArgs eventArgs)
		{
			//FacebookStateManager.Instance.OnLoggedOut();
			InvokeOnMainThread(() =>
			{
				SetupViewForNotLoggedIn();
			});
		}

	}
}