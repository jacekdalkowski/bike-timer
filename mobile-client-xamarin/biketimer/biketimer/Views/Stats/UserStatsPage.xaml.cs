using System;
using System.Collections.Generic;
using Biketimer.BiketimerApiServer.Entities;
using Xamarin.Forms;
using System.Linq;
using Biketimer.Views.Helpers;

namespace Biketimer.Views.Stats
{
	public partial class UserStatsPage : ContentPage
	{
		private readonly UserStatsPageModel _viewModel = new UserStatsPageModel();

		private readonly StatsPage _parentStatsPage;

		public ListView ListView { get { return listView; } }
		public ActivityIndicator ActivityIndicator { get { return activityIndicator; } }

		public Button FilterByDateButton { get { return filterByDateButton; } }
		public Button FilterBySpotButton { get { return filterBySpotButton; } }
		public Button FilterByTrackButton { get { return filterByTrackButton; } }
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
			FilterByTrackButton.Clicked += OnFilterByTrackClicked;
			FilterBySegmentButton.Clicked += OnFilterBySegmentClicked;
			SortButton.Clicked += OnSortClicked;

			_viewModel.IsLoadingInitData = true;

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
			_viewModel.SetSpotsData(spotsData);
			_viewModel.IsLoadingInitData = false;
		}

		async void OnFilterByDateClicked(object sender, EventArgs e)
		{
			string[] periods = new string[] { "Today", "Last 2 days", "Last week" };
			string selectedSpot = await DisplayActionSheet("Period", "Cancel", null, periods);
		}

		async void OnFilterBySpotClicked(object sender, EventArgs e)
		{
			Tuple<string, string> selectedValue = await this.DisplayKeyValueActionSheet("Spot", "Cancel", null, _viewModel.FilteringSpotsList);
			if (selectedValue != null)
			{
				_viewModel.FilteringSpot = selectedValue;
			}
		}

		async void OnFilterByTrackClicked(object sender, EventArgs e)
		{
			if (_viewModel.IsFilteringSpotSet)
			{
				Tuple<string, string> selectedValue = await this.DisplayKeyValueActionSheet("Track", "Cancel", null, _viewModel.FilteringTracksList);
				if (selectedValue != null)
				{
					_viewModel.FilteringTrack = selectedValue;
				}
			}
		}

		async void OnFilterBySegmentClicked(object sender, EventArgs e)
		{
			if (_viewModel.IsFilteringTrackSet)
			{
				Tuple<string, string> selectedValue = await this.DisplayKeyValueActionSheet("Segment", "Cancel", null, _viewModel.FilteringSegmentsList);
				if (selectedValue != null)
				{
					_viewModel.FilteringSegment = selectedValue;
				}
			}
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

