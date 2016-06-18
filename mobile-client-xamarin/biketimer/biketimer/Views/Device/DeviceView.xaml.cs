using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Device
{
	public partial class DeviceView : ContentPage
	{
		public DeviceView()
		{
			InitializeComponent();
			devicesListView.ItemsSource = PlatformSpecificManagers.BluetoothManager.Devices;
		}
	}
}

