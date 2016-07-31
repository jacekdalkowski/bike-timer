using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Account
{
	public partial class AccountsList : ContentPage
	{
		public ListView ListView { get { return listView; } }
		private NavigationPage _topNavigationPage;

		public AccountsList(NavigationPage topNavigationPage)
		{
			_topNavigationPage = topNavigationPage;

			InitializeComponent();
			ListView.ItemsSource = new AccountsListItem[] 
			{
				new AccountsListItem
				{
					Title = "Facebook",
					TargetViewType = typeof(FacebookAccountDebugPage),
					TargetViewModelType = typeof(FacebookAccountDebugPageViewModel)
				},
				new AccountsListItem
				{
					Title = "Biketimer",
					TargetViewType = typeof(BiketimerAccountDebugPage),
					TargetViewModelType = typeof(BiketimerAccountDebugPageViewModel)
				}
			};

			ListView.ItemSelected += OnItemSelected;
		}

		void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
		{
			AccountsListItem item = e.SelectedItem as AccountsListItem;
			if (item != null)
			{
				Object viewModel = Activator.CreateInstance(item.TargetViewModelType);
				Page page = (Page)Activator.CreateInstance(item.TargetViewType, viewModel);
				_topNavigationPage.PushAsync(page);
				ListView.SelectedItem = null;
			}
		}
	}

	public class AccountsListItem
	{
		public string Title { get; set; } 
		public Type TargetViewType { get; set; }
		public Type TargetViewModelType { get; set; }
	}
}

