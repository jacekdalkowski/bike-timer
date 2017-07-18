using System;
using System.Collections.Generic;
using Biketimer.BiketimerApiServer.Entities;
using Xamarin.Forms;
using System.Linq;
using Biketimer.Views.Helpers;
using Biketimer.BiketimerApiServer;
using Biketimer.Account;

namespace Biketimer.Views.Stats
{
	public partial class UserStatsPage : ContentPage
	{
		// TBD: Do I need that?
		private readonly StatsPage _parentStatsPage;

		private readonly StatsPageModel _statsPageModel;

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
			_statsPageModel = parentStatsPage.Model;

			Title = "Me";

			InitializeComponent();

			FilterByDateButton.Clicked += OnFilterByDateClicked;
			FilterBySpotButton.Clicked += OnFilterBySpotClicked;
			FilterByTrackButton.Clicked += OnFilterByTrackClicked;
			FilterBySegmentButton.Clicked += OnFilterBySegmentClicked;
			SortButton.Clicked += OnSortClicked;

			// TBD: Do I need that?
			//_statsPageModel.PropertyChanged += OnViewModelChanged;

			BindingContext = _statsPageModel;
		}

		/*
		async void OnViewModelChanged(object sender, System.ComponentModel.PropertyChangedEventArgs e)
		{
			string userId = AccountManager.Instance.AccountData.BiketimerAccountData.Profile.Id;
			string filteringQuery = BiketimerFacadeQueryBuilder.BuildRunsQuery(userId,
			                                                                   _statsPageModel.Filtering.FilteringSpot != null ? _statsPageModel.Filtering.FilteringSpot.Item2 : null,
_statsPageModel.Filtering.FilteringTrack != null ? _statsPageModel.Filtering.FilteringTrack.Item2 : null,
			       _statsPageModel.Filtering.FilteringSegment != null ? _statsPageModel.Filtering.FilteringSegment.Item2 : null,
                   null, 
                   null);
		}
		*/

		async void OnFilterByDateClicked(object sender, EventArgs e)
		{
			string[] periods = new string[] { "Today", "Last 2 days", "Last week" };
			string selectedSpot = await DisplayActionSheet("Period", "Cancel", null, periods);
		}

		async void OnFilterBySpotClicked(object sender, EventArgs e)
		{
			Tuple<string, string> selectedValue = await this.DisplayKeyValueActionSheet("Spot", "Cancel", null, _statsPageModel.Filtering.FilteringSpotsList);
			if (selectedValue != null)
			{
				_statsPageModel.Filtering.FilteringSpot = selectedValue;
			}
		}

		async void OnFilterByTrackClicked(object sender, EventArgs e)
		{
			if (_statsPageModel.Filtering.IsFilteringSpotSet)
			{
				Tuple<string, string> selectedValue = await this.DisplayKeyValueActionSheet("Track", "Cancel", null, _statsPageModel.Filtering.FilteringTracksList);
				if (selectedValue != null)
				{
					_statsPageModel.Filtering.FilteringTrack = selectedValue;
				}
			}
		}

		async void OnFilterBySegmentClicked(object sender, EventArgs e)
		{
			if (_statsPageModel.Filtering.IsFilteringTrackSet)
			{
				Tuple<string, string> selectedValue = await this.DisplayKeyValueActionSheet("Segment", "Cancel", null, _statsPageModel.Filtering.FilteringSegmentsList);
				if (selectedValue != null)
				{
					_statsPageModel.Filtering.FilteringSegment = selectedValue;
				}
			}
		}

		async void OnSortClicked(object sender, EventArgs e)
		{
			Tuple<string, string> selectedValue = await this.DisplayKeyValueActionSheet("Sort by", "Cancel", null, _statsPageModel.Filtering.SortingOptionsList);
			if (selectedValue != null)
			{
				_statsPageModel.Filtering.SortingOption = selectedValue;
			}
			
		}

		public class RunItem
		{
			public string Title { get; set; }
		}
	}
}

