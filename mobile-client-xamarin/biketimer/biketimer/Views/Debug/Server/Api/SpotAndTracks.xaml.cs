using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Server.Api
{
	public partial class SpotAndTracks : ContentPage
	{
		public ListView CurrentTracksListView { get { return currentTracksList; } }
		public ListView OldTracksListView { get { return oldTracksList; } }

		public SpotAndTracks(NavigationPage topNavigationPage, Spot spot)
		{
			InitializeComponent();
			SpotAndTracksViewModel viewModel = new SpotAndTracksViewModel(spot);
			BindingContext = viewModel;

			CurrentTracksListView.ItemsSource = spot.TracksCurrent;
			OldTracksListView.ItemsSource = spot.TracksOld;
		}
	}
}

