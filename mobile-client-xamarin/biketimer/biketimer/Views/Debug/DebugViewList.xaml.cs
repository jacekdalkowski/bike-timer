using System;
using System.Collections.Generic;
using Biketimer.Views.Debug.Account;
using Xamarin.Forms;

namespace Biketimer.Views.Debug
{
	public partial class DebugViewList : ContentPage
	{
		public ListView ListView { get { return listView; } }
		private readonly NavigationPage _topNavigationPage;

		public DebugViewList(NavigationPage topNavigationPage)
		{
			_topNavigationPage = topNavigationPage;

			InitializeComponent();
			ListView.ItemsSource = new DebugListItem[]
			{
				new DebugListItem
				{
					Title = "Account",
					ViewType = typeof(AccountsList)
				},
				new DebugListItem
				{
					Title = "Servers",
					ViewType = typeof(ServersList)
				}
			};
			ListView.ItemSelected += OnItemSelected;
		}

		void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
		{
			DebugListItem item = e.SelectedItem as DebugListItem;
			if (item != null)
			{
				Page page = (Page)Activator.CreateInstance(item.ViewType, _topNavigationPage);
				_topNavigationPage.PushAsync(page);
				ListView.SelectedItem = null;
			}
		}
	}

	public class DebugListItem
	{
		public string Title { get; set; }
		public Type ViewType { get; set; }
	}
}

