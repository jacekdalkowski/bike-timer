using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Server.Api
{
	public partial class ApiResourcesList : ContentPage
	{
		public ListView ListView { get { return listView; } }
		private NavigationPage _topNavigationPage;

		public ApiResourcesList(NavigationPage topNavigationPage)
		{
			_topNavigationPage = topNavigationPage;

			InitializeComponent();
			ListView.ItemsSource = new ApiResourcesListItem[]
			{
				new ApiResourcesListItem
				{
					Title = "Spots",
					TargetViewType = typeof(Spots)
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
			ApiResourcesListItem item = e.SelectedItem as ApiResourcesListItem;
			if (item != null)
			{
				Page page = (Page)Activator.CreateInstance(item.TargetViewType);
				_topNavigationPage.PushAsync(page);
				ListView.SelectedItem = null;
			}
		}
	}

	public class ApiResourcesListItem
	{
		public string Title { get; set; }
		public Type TargetViewType { get; set; }
	}
}

