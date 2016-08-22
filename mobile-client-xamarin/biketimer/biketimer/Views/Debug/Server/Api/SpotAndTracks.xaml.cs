using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Server.Api
{
	public partial class SpotAndTracks : ContentPage
	{
		public ListView CurrentTracksListView { get { return currentTracksList; } }
		public ListView OldTracksListView { get { return oldTracksList; } }
		private NavigationPage _topNavigationPage;

		public SpotAndTracks(NavigationPage topNavigationPage, Spot spot)
		{
			_topNavigationPage = topNavigationPage;

			InitializeComponent();
			SpotAndTracksViewModel viewModel = new SpotAndTracksViewModel(spot);
			BindingContext = viewModel;

			CurrentTracksListView.ItemsSource = spot.TracksCurrent;
			CurrentTracksListView.ItemSelected += (sender, e) => OnTrackSelected(sender, e, CurrentTracksListView);

			OldTracksListView.ItemsSource = spot.TracksOld;
			OldTracksListView.ItemSelected += (sender, e) => OnTrackSelected(sender, e, OldTracksListView);
		}

		void OnTrackSelected(object sender, SelectedItemChangedEventArgs e, ListView listView)
		{
			Track selectedTrack = e.SelectedItem as Track;
			if (selectedTrack != null)
			{
				Page page = new TrackAndSegments(_topNavigationPage, selectedTrack);
				_topNavigationPage.PushAsync(page);
				listView.SelectedItem = null;
			}
		}
	}
}

