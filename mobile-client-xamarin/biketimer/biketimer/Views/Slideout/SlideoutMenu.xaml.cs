using System;
using System.Collections.Generic;
using Xamarin.Forms;
using Biketimer.Views.Login;
using Biketimer.Views.Device;
using Biketimer.Views.Stats;
using Biketimer.Views.Debug;

namespace Biketimer.Views.Slideout
{
	public partial class SlideoutMenu : ContentPage
	{
		public ListView ListView { get { return listView; } }

		public SlideoutMenu()
		{
			InitializeComponent();

			var masterPageItems = new List<SlideoutMenuItem>();
			masterPageItems.Add(new SlideoutMenuItem
			{
				Title = "Login",
				IconSource = "contacts.png",
				TargetType = typeof(LoginView)
			});
			masterPageItems.Add(new SlideoutMenuItem
			{
				Title = "Device",
				IconSource = "todo.png",
				TargetType = typeof(DeviceView)
			});
			masterPageItems.Add(new SlideoutMenuItem
			{
				Title = "Stats",
				IconSource = "reminders.png",
				TargetType = typeof(StatsView)
			});
			masterPageItems.Add(new SlideoutMenuItem
			{
				Title = "Debug",
				IconSource = "reminders.png",
				TargetType = typeof(DebugView)
			});

			listView.ItemsSource = masterPageItems;
		}
	}
}

