using System;
using Biketimer.Bluetooth;
using Biketimer.Facebook;

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

		private static FacebookStateManagerCommon _facebookStateManagerCommon;
		public static FacebookStateManagerCommon FacebookStateManager
		{
			get
			{
				return _facebookStateManagerCommon;
			}
			set
			{
				if (_facebookStateManagerCommon != null)
				{
					throw new InvalidOperationException("Facebook manager already set.");
				}
				_facebookStateManagerCommon = value;
			}
		}
	}
}

