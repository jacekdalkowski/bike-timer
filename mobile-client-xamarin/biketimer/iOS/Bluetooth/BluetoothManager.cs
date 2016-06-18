using System;
using System.Collections.ObjectModel;
using Robotics.Mobile.Core.Bluetooth.LE;
using System.Threading.Tasks;
using System.Collections.Generic;
using Biketimer.Bluetooth;
using System.Linq;

namespace Biketimer.iOS
{
	public class BluetoothManager : Biketimer.Bluetooth.IBluetoothManager
	{
		private IAdapter _bluetoothAdapter;
		private ObservableCollection<DeviceInfo> _devices;

		public BluetoothManager(IAdapter adapter)
		{
			this._bluetoothAdapter = adapter;
			this._devices = new ObservableCollection<DeviceInfo>();
			_devices.Add(new DeviceInfo() 
			{ 
				ID = Guid.NewGuid().ToString(),
				Name = "Fake device"
			});

			_bluetoothAdapter.DeviceDiscovered += (object sender, DeviceDiscoveredEventArgs e) =>
			{
				Xamarin.Forms.Device.BeginInvokeOnMainThread(() => _devices.Add(new DeviceInfo()
				{
					ID = e.Device.ID.ToString(),
					Name = e.Device.Name
				}));
			};

			_bluetoothAdapter.StartScanningForDevices(Guid.Empty);
		}

		public ObservableCollection<DeviceInfo> Devices 
		{ 
			get
			{
				return _devices;
			}
		}
	}
}

