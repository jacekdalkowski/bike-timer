using System;
using System.Collections.Generic;
using System.Linq;

using Foundation;
using UIKit;
using FacebookCoreKit = Facebook.CoreKit;

using Robotics.Mobile.Core.Bluetooth.LE;

using Biketimer.iOS.LocalStorage;

namespace Biketimer.iOS
{
	[Register ("AppDelegate")]
	public partial class AppDelegate : global::Xamarin.Forms.Platform.iOS.FormsApplicationDelegate
	{
		private UIApplication _iOSApp;
		private Biketimer.App _formsApp;

		public override bool FinishedLaunching (UIApplication iOSApp, NSDictionary options)
		{
			_iOSApp = iOSApp;

			global::Xamarin.Forms.Forms.Init();

			var bluetoothManager = new BluetoothManager(Adapter.Current);
			var localStorageManager = new LocalStorageManager();
			_formsApp = new Biketimer.App(bluetoothManager, localStorageManager);
			LoadApplication(_formsApp);

			FacebookSetupOnFinishedLaunching(options, localStorageManager);

			return base.FinishedLaunching (iOSApp, options);
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

