using System;
using Xamarin.Forms;
using Biketimer.Bluetooth;
using Biketimer.Facebook;

namespace Biketimer
{
	public class App : Application
	{
		private IBluetoothManager _bluetoothManager;

		public App (IBluetoothManager bluetoothManager, FacebookStateManagerCommon facebookStateManager)
		{
			PlatformSpecificManagers.BluetoothManager = bluetoothManager;
			PlatformSpecificManagers.FacebookStateManager = facebookStateManager;
			MainPage = new Biketimer.Views.Slideout.SlideoutNavigation();
		}

		protected override void OnStart ()
		{
			// Handle when your app starts
		}

		protected override void OnSleep ()
		{
			// Handle when your app sleeps
		}

		protected override void OnResume ()
		{
			// Handle when your app resumes
		}
	}
}

