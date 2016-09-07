using System;
using Xamarin.Forms;
using Biketimer.Bluetooth;
using Biketimer.LocalStorage;

namespace Biketimer
{
	public class App : Application
	{
		// TODO
		public static App Instance;

		public App (IBluetoothManager bluetoothManager, ILocalStorageManager localStorageManager)
		{
			Instance = this;
			PlatformSpecificManagers.BluetoothManager = bluetoothManager;
			PlatformSpecificManagers.LocalStorageManager = localStorageManager;
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

