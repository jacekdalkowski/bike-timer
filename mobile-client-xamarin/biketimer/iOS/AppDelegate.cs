using System;
using System.Collections.Generic;
using System.Linq;

using Foundation;
using UIKit;
using FacebookCoreKit = Facebook.CoreKit;

using Robotics.Mobile.Core.Bluetooth.LE;

namespace Biketimer.iOS
{
	[Register ("AppDelegate")]
	public partial class AppDelegate : global::Xamarin.Forms.Platform.iOS.FormsApplicationDelegate
	{
		public override bool FinishedLaunching (UIApplication app, NSDictionary options)
		{
			global::Xamarin.Forms.Forms.Init ();

			var bluetoothManager = new BluetoothManager(Adapter.Current);
			var facebookStateManager = FacebookStateManager.Instance;
			var commonApp = new Biketimer.App(bluetoothManager, facebookStateManager);
			LoadApplication(commonApp);

			FacebookSetupOnFinishedLaunching(app, options);

			return base.FinishedLaunching (app, options);
		}

		public override bool OpenUrl(UIApplication application, NSUrl url, string sourceApplication, NSObject annotation)
		{
			// We need to handle URLs by passing them to their own OpenUrl in order to make the SSO authentication works.
			return FacebookCoreKit.ApplicationDelegate.SharedInstance.OpenUrl(application, url, sourceApplication, annotation);
			//return true;
		}

		public override void OnActivated(UIKit.UIApplication uiApplication)
		{
			base.OnActivated(uiApplication);
			FacebookCoreKit.AppEvents.ActivateApp();
		}
	}
}

