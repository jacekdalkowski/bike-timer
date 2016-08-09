using System;
using System.Collections.Generic;
using Biketimer.Account;
using Xamarin.Forms;

namespace Biketimer
{
	public partial class AppDataView : ContentPage
	{
		public AppDataView(NavigationPage topNavigationPage)
		{
			InitializeComponent();
			AccountData accountData = null;
			if (App.Instance.Properties.ContainsKey("accountData"))
			{
				accountData = App.Instance.Properties["accountData"] as AccountData;
			}
			BindingContext = new AppDataViewModel(accountData);
		}
	}
}

