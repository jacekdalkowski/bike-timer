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

		public StatsPageModel Model { get; private set; }

		public StatsPage()
		{
			Model = new StatsPageModel();
			Model.Load();

			this.Children.Add(new UserStatsPage(this));
			this.Children.Add(new FriendsStatsPage(this));
			this.Children.Add(new SpotsStatsPage(this));
		}

		//private void LoadFilterData()
		//{
		//	BiketimerFacade biketimerFacade = new BiketimerFacade(Config.BiketimerApiDomainUrl);
		//	string biketimerApiAccessToken = AccountManager.Instance.AccountData.BiketimerAccountData.Access.AccessToken;
		//	biketimerFacade.GetSpots(biketimerApiAccessToken)
		//				   .ContinueWith(t => OnFilterDataFetched(t.Result));
		//}
	}
}

