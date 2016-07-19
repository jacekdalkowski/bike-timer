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
				Page page = (Page)Activator.CreateInstance(item.TargetType);
				if (page is NavigationPage)
				{
					Detail = page;
				}
				else 
				{
					Detail = new NavigationPage(page);
				}
				slideoutMenu.ListView.SelectedItem = null;
				IsPresented = false;
			}
		}
	}
}

