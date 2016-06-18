using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Slideout
{
	public partial class SlideoutNavigation : MasterDetailPage
	{
		public SlideoutNavigation()
		{
			InitializeComponent();
			slideoutMenu.ListView.ItemSelected += OnItemSelected;
		}

		void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
		{
			var item = e.SelectedItem as SlideoutMenuItem;
			if (item != null)
			{
				Detail = new NavigationPage((Page)Activator.CreateInstance(item.TargetType));
				slideoutMenu.ListView.SelectedItem = null;
				IsPresented = false;
			}
		}
	}
}

