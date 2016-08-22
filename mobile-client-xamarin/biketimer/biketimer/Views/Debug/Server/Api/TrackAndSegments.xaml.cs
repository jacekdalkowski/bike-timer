using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Server.Api
{
	public partial class TrackAndSegments : ContentPage
	{
		public ListView CurrentSegmentsListView { get { return currentSegmentsList; } }
		public ListView OldSegmentsListView { get { return oldSegmentsList; } }
		private NavigationPage _topNavigationPage;

		public TrackAndSegments(NavigationPage topNavigationPage, Track track)
		{
			_topNavigationPage = topNavigationPage;

			InitializeComponent();
			TrackAndSegmentsViewModel viewModel = new TrackAndSegmentsViewModel(track);
			BindingContext = viewModel;

			CurrentSegmentsListView.ItemsSource = track.SegmentsCurrent;
			CurrentSegmentsListView.ItemSelected += (sender, e) => OnSegmentSelected(sender, e, CurrentSegmentsListView);

			OldSegmentsListView.ItemsSource = track.SegmentsOld;
			OldSegmentsListView.ItemSelected += (sender, e) => OnSegmentSelected(sender, e, OldSegmentsListView);
		}

		void OnSegmentSelected(object sender, SelectedItemChangedEventArgs e, ListView listView)
		{
			Biketimer.Segment selectedSegment = e.SelectedItem as Biketimer.Segment;
			if (selectedSegment != null)
			{
				Page page = new Segment(_topNavigationPage, selectedSegment);
				_topNavigationPage.PushAsync(page);
				listView.SelectedItem = null;
			}
		}
	}
}

