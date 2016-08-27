using System;
using System.Collections.Generic;
using Biketimer.BiketimerApiServer.Entities;
using Xamarin.Forms;
using System.Linq;

namespace Biketimer.Views.Stats
{
	public partial class UserStatsPage : ContentPage
	{
		private readonly UserStatsPageModel _viewModel = new UserStatsPageModel();

		private readonly StatsPage _parentStatsPage;
		private IEnumerable<Spot> _spotsData;

		public ListView ListView { get { return listView; } }
		public ActivityIndicator ActivityIndicator { get { return activityIndicator; } }

		public Button FilterByDateButton { get { return filterByDateButton; } }
		public Button FilterBySpotButton { get { return filterBySpotButton; } }
		public Button FilterBySegmentButton { get { return filterBySegmentButton; } }
		public Button SortButton { get { return sortButton; } }

		public UserStatsPage(StatsPage parentStatsPage)
		{
			_parentStatsPage = parentStatsPage;

			Title = "Me";

			InitializeComponent();

			parentStatsPage.OnFilterDataFetched += OnFilterDataFetched;
			FilterByDateButton.Clicked += OnFilterByDateClicked;
			FilterBySpotButton.Clicked += OnFilterBySpotClicked;
			FilterBySegmentButton.Clicked += OnFilterBySegmentClicked;
			SortButton.Clicked += OnSortClicked;

			ActivityIndicator.IsVisible = true;
			ActivityIndicator.IsRunning = true;

			BindingContext = _viewModel;

			ListView.ItemsSource = new RunItem[]
			{
				new RunItem { Title = "AAA" },
				new RunItem { Title = "BBB" },
				new RunItem { Title = "CCC" }
			};
		}

		void OnFilterDataFetched(IEnumerable<Spot> spotsData)
		{
			_spotsData = spotsData;
			ActivityIndicator.IsVisible = false;
			ActivityIndicator.IsRunning = false;
		}

		async void OnFilterByDateClicked(object sender, EventArgs e)
		{
			string[] spots = new string[] { "Today", "Last 2 days", "Last week" };
			string selectedSpot = await DisplayActionSheet("Period", "Cancel", null, spots);
		}

		async void OnFilterBySpotClicked(object sender, EventArgs e)
		{
			if (_spotsData != null)
			{
				string[] allSpots = new string[] { "All" };
				IEnumerable<string> spots = _spotsData.Select(s => s.Name);
				string[] spotFilterChoices = allSpots.Concat(spots).ToArray();
				_viewModel.FilteringSpot = await DisplayActionSheet("Spot", "Cancel", null, spotFilterChoices);
			}
			else
			{
				throw new Exception("Filter by spot button should not be active when spots data is not fetched.");
			}
		}

		async void OnFilterBySegmentClicked(object sender, EventArgs e)
		{
			string[] segments = new string[] { "Meadow", "Forest" };
			string selectedSegment = await DisplayActionSheet("Segment", "Cancel", null, segments);
		}

		async void OnSortClicked(object sender, EventArgs e)
		{
			string[] segments = new string[] { "Time", "Date - current first", "Date - oldest first" };
			var action = await DisplayActionSheet("Sort by", "Cancel", null, segments);
		}

		public class RunItem
		{
			public string Title { get; set; }
		}
	}
}

