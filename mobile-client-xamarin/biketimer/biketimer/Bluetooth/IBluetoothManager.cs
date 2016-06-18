using System;
using System.Collections.ObjectModel;

namespace Biketimer.Bluetooth
{
	public interface IBluetoothManager
	{
		ObservableCollection<DeviceInfo> Devices { get; }
	}

	public class DeviceInfo
	{
		public string Name { get; set; }
		public string ID { get; set; }
	}
}

