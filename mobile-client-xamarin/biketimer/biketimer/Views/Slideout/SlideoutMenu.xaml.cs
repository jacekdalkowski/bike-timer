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

		private List<SlideoutMenuItem> _menuForLoggedInUser;
		private List<SlideoutMenuItem> _menuForNotLoggedInUser;

		public SlideoutMenu()
		{
			InitializeComponent();
			_menuForLoggedInUser = CreateMenuForLoggedInUser();
			_menuForNotLoggedInUser = CreateMenuForNotLoggedInUser();

			PlatformSpecificManagers.FacebookStateManager.LoginCompleted += OnLoginCompleted;

			listView.ItemsSource = _menuForNotLoggedInUser;
		}

		private void OnLoginCompleted(FacebookAccount facebookAccessData)
		{
			Xamarin.Forms.Device.BeginInvokeOnMainThread(() => listView.ItemsSource = _menuForLoggedInUser);
		}

		private static List<SlideoutMenuItem> CreateMenuForLoggedInUser()
		{
			var menuItems = new List<SlideoutMenuItem>()
			{
				new SlideoutMenuItem
				{
					Title = "Login",
					IconSource = "contacts.png",
					TargetType = typeof(LoginView)
				},
				new SlideoutMenuItem
				{
					Title = "Device",
					IconSource = "todo.png",
					TargetType = typeof(DeviceView)
				},
				new SlideoutMenuItem
				{
					Title = "Stats",
					IconSource = "reminders.png",
					TargetType = typeof(StatsView)
				},
				new SlideoutMenuItem
				{
					Title = "Debug",
					IconSource = "reminders.png",
					TargetType = typeof(DebugView)
				}
			};
			return menuItems;
		}

		private static List<SlideoutMenuItem> CreateMenuForNotLoggedInUser()
		{
			var menuItems = new List<SlideoutMenuItem>()
			{
				new SlideoutMenuItem
				{
					Title = "Login",
					IconSource = "contacts.png",
					TargetType = typeof(LoginView)
				}
			};
			return menuItems;
		}
	}
}

