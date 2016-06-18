using System;
using System.Collections.Generic;
using System.Linq;

using Foundation;
using UIKit;

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
			var commonApp = new Biketimer.App(bluetoothManager);
			LoadApplication(commonApp);

			return base.FinishedLaunching (app, options);
		}
	}
}

