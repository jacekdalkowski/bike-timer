using System;
using System.Collections.Generic;
using Xamarin.Forms;
using Biketimer.BiketimerApiServer;
using System.Threading.Tasks;
using System.Collections.ObjectModel;
using Biketimer.Account;

namespace Biketimer.Views.Debug.Server.Api
{
	public partial class Spots : ContentPage
	{
		private SpotsViewModel _spotsViewModel;
		private NavigationPage _topNavigationPage;

		public ListView ListView { get { return listView; } }
		public ActivityIndicator ActivityIndicator { get { return activityIndicator; } }

		public Spots(NavigationPage topNavigationPage)
		{
			_topNavigationPage = topNavigationPage;

			InitializeComponent();
			_spotsViewModel = new SpotsViewModel();
			_spotsViewModel.IsBusy = true;
			BindingContext = _spotsViewModel;
			ListView.ItemSelected += OnSpotSelected;
			ActivityIndicator.IsVisible = true;
			ActivityIndicator.IsRunning = true;

			ListView.ItemsSource = new ObservableCollection<Spot>();

			if (AccountManager.Instance.AccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData.Access != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData.Access.AccessToken != null)
			{
				BiketimerFacade biketimerFacade = new BiketimerFacade();
				biketimerFacade.GetSpots(AccountManager.Instance.AccountData.BiketimerAccountData.Access.AccessToken)
							   .ContinueWith(OnSpotsDownloaded);
			}
		}

		void OnSpotSelected(object sender, SelectedItemChangedEventArgs e)
		{
			Spot selectedSpot = e.SelectedItem as Spot;
			if (selectedSpot != null)
			{
				Page page = new SpotAndTracks(_topNavigationPage, selectedSpot);
				_topNavigationPage.PushAsync(page);
				ListView.SelectedItem = null;
			}
		}

		private void OnSpotsDownloaded(Task<IEnumerable<Spot>> spotsTask)
		{
			ActivityIndicator.IsVisible = false;
			ActivityIndicator.IsRunning = false;

			IEnumerable<Spot> spots = spotsTask.Result;
			ObservableCollection<Spot> spotsInList = (ObservableCollection<Spot>)ListView.ItemsSource;
			spotsInList.Clear();
			foreach (Spot spot in spots)
			{
				spotsInList.Add(spot);
			}
		}
	}
}

