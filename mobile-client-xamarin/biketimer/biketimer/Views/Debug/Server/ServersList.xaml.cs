using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer
{
	public partial class ServersList : ContentPage
	{
		public ListView ListView { get { return listView; } }
		private NavigationPage _topNavigationPage;

		public ServersList(NavigationPage topNavigationPage)
		{
			_topNavigationPage = topNavigationPage;

			InitializeComponent();
			ListView.ItemsSource = new ServersListItem[]
			{
				new ServersListItem
				{
					Title = "Api resources",
					TargetViewType = typeof(Biketimer.Views.Debug.Server.Api.ApiResourcesList)
				}/*,
				new AccountsListItem
				{
					Title = "Identity",
					TargetViewType = typeof(BiketimerAccountDebugPage)
				}*/
			};

			ListView.ItemSelected += OnItemSelected;
		}

		void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
		{
			ServersListItem item = e.SelectedItem as ServersListItem;
			if (item != null)
			{
				Page page = (Page)Activator.CreateInstance(item.TargetViewType, _topNavigationPage);
				_topNavigationPage.PushAsync(page);
				ListView.SelectedItem = null;
			}
		}
	}

	public class ServersListItem
	{
		public string Title { get; set; }
		public Type TargetViewType { get; set; }
	}
}

