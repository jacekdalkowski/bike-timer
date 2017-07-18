using System;
using System.Collections.Generic;
using Biketimer.Account;
using Biketimer.BiketimerApiServer;
using Biketimer.BiketimerApiServer.Entities;
using Biketimer.Views.Stats.Common.Filtering;
using Biketimer.Views.Stats.Tabs.Friends;
using Biketimer.Views.Stats.Tabs.Spots;
using Biketimer.Views.Stats.Tabs.User;

namespace Biketimer.Views.Stats
{
	public class StatsPageModel
	{
		public FilteringModel Filtering { get; private set; }
		public UserStatsPageModel User { get; private set; }
		public FriendsStatsPageModel Friends { get; private set; }
		public SpotsStatsPageModel Spots { get; private set; }

		public StatsPageModel()
		{
			Filtering = new FilteringModel();
			User = new UserStatsPageModel();
			Friends = new FriendsStatsPageModel();
			Spots = new SpotsStatsPageModel();
		}

		public void Load()
		{
			Filtering.Load();
		}
	}
}
