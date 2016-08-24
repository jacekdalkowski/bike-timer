using System;
using Xamarin.Forms;

namespace Biketimer.Views.Stats
{
	public class StatsPage : TabbedPage
	{
		public StatsPage()
		{
			this.Children.Add(new UserStatsPage());
			this.Children.Add(new FriendsStatsPage());
			this.Children.Add(new SpotsStatsPage());
		}
	}
}

