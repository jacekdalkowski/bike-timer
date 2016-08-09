using System;
using Xamarin.Forms;
using Biketimer.Bluetooth;

namespace Biketimer
{
	public class App : Application
	{
		// TODO
		public static App Instance;

		private IBluetoothManager _bluetoothManager;

		public App (IBluetoothManager bluetoothManager)
		{
			Instance = this;
			PlatformSpecificManagers.BluetoothManager = bluetoothManager;
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

