using System;
using System.Collections.Generic;
using Biketimer.BiketimerApiServer.Entities;
using Xamarin.Forms;

namespace Biketimer.Views.Stats
{
	public partial class FriendsStatsPage : ContentPage
	{
		private readonly StatsPage _parentStatsPage;

		public ActivityIndicator ActivityIndicator { get { return activityIndicator; } }

		public FriendsStatsPage(StatsPage parentStatsPage)
		{
			_parentStatsPage = parentStatsPage;
			parentStatsPage.OnFilterDataFetched += OnFilterDataFetched;

			Title = "Friends";
			InitializeComponent();
		}

		void OnFilterDataFetched(IEnumerable<Spot> spots)
		{

		}
	}
}

