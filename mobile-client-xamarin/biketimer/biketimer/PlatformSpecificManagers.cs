using System;
using Biketimer.Bluetooth;
using Biketimer.LocalStorage;

namespace Biketimer
{
	public class PlatformSpecificManagers
	{
		private static IBluetoothManager _bluetoothManager;
		public static IBluetoothManager BluetoothManager
		{
			get
			{
				return _bluetoothManager;
			}
			set
			{
				if (_bluetoothManager != null)
				{
					throw new InvalidOperationException("Bluetooth manager already set.");
				}
				_bluetoothManager = value;
			}
		}

		private static ILocalStorageManager _localStorageManager;
		public static ILocalStorageManager LocalStorageManager
		{
			get
			{
				return _localStorageManager;
			}
			set
			{
				if (_localStorageManager != null)
				{
					throw new InvalidOperationException("Local storage manager already set.");
				}
				_localStorageManager = value;
			}
		}
	}
}

