using System;
using System.Collections.Generic;
using Biketimer.Account;
using Biketimer.BiketimerApiServer;
using Biketimer.BiketimerApiServer.Entities;
using Xamarin.Forms;

namespace Biketimer.Views.Stats
{
	public class StatsPage : TabbedPage
	{
		public event Action<IEnumerable<Spot>> OnFilterDataFetched;

		public StatsPage()
		{
			this.Children.Add(new UserStatsPage(this));
			this.Children.Add(new FriendsStatsPage(this));
			this.Children.Add(new SpotsStatsPage(this));

			LoadFilterData();
		}

		private void LoadFilterData()
		{
			BiketimerFacade biketimerFacade = new BiketimerFacade();
			string biketimerApiAccessToken = AccountManager.Instance.AccountData.BiketimerAccountData.Access.AccessToken;
			biketimerFacade.GetSpots(biketimerApiAccessToken)
						   .ContinueWith(t => OnFilterDataFetched(t.Result));
		}
	}
}

