using System;
using System.Collections.Generic;
using Biketimer.Account;
using Biketimer.BiketimerApiServer;
using Biketimer.BiketimerApiServer.Entities;

namespace Biketimer.Views.Stats.Common.Filtering
{
	public partial class FilteringModel
	{
		private bool _isLoading;
		public bool IsLoading
		{
			set
			{
				if (_isLoading != value)
				{
					_isLoading = value;
					IsLoaded = !_isLoading;
					OnPropertyChanged("IsLoading");
				}
			}
			get
			{
				return _isLoading;
			}
		}
		public bool IsLoaded
		{
			set
			{
				OnPropertyChanged("IsLoaded");
			}
			get
			{
				return !IsLoading;
			}
		}

		public void Load()
		{
			BiketimerFacade biketimerFacade = new BiketimerFacade(Config.BiketimerApiDomainUrl);
			string biketimerApiAccessToken = AccountManager.Instance.AccountData.BiketimerAccountData.Access.AccessToken;
			biketimerFacade.GetSpots(biketimerApiAccessToken)
				   .ContinueWith(t => OnFilterDataFetched(t.Result));

		}

		void OnFilterDataFetched(IEnumerable<Spot> spotsData)
		{
			SetSpotsData(spotsData);
		}
	}
}
