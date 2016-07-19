using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Account
{
	public partial class AccountsList : ContentPage
	{
		public ListView ListView { get { return listView; } }

		public AccountsList()
		{
			InitializeComponent();
			ListView.ItemsSource = new AccountsListItem[] 
			{
				new AccountsListItem
				{
					Title = "Facebook"
				},
				new AccountsListItem
				{
					Title = "Biketimer"
				}
			};
		}
	}

	public class AccountsListItem
	{
		public string Title { get; set; } 
	}
}

