using System;
using Biketimer.Bluetooth;

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

	}
}

