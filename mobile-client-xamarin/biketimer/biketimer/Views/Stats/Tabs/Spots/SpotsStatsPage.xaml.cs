using System;
using System.Collections.Generic;
using Biketimer.BiketimerApiServer.Entities;
using Xamarin.Forms;

namespace Biketimer.Views.Stats
{
	public partial class SpotsStatsPage : ContentPage
	{
		private readonly StatsPage _parentStatsPage;

		public ActivityIndicator ActivityIndicator { get { return activityIndicator; } }

		public SpotsStatsPage(StatsPage parentStatsPage)
		{
			_parentStatsPage = parentStatsPage;
			parentStatsPage.OnFilterDataFetched += OnFilterDataFetched;

			Title = "Spots";
			InitializeComponent();
		}

		void OnFilterDataFetched(IEnumerable<Spot> spots)
		{

		}
	}
}

