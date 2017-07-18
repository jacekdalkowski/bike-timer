using System;
using System.Collections.Generic;
using System.ComponentModel;
using Biketimer.Account;
using Biketimer.BiketimerApiServer;
using Biketimer.BiketimerApiServer.Entities;

namespace Biketimer.Views.Stats.Common.Filtering
{
	public partial class FilteringModel
	{

		public event PropertyChangedEventHandler PropertyChanged;

		private IEnumerable<Spot> _spotsData;

		protected virtual void OnPropertyChanged(string propertyName)
		{
			if (PropertyChanged != null)
			{
				PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
			}
		}

		async void OnFilteringChanged()
		{
			string userId = AccountManager.Instance.AccountData.BiketimerAccountData.Profile.Id;
			string filteringQuery = BiketimerFacadeQueryBuilder.BuildRunsQuery(userId,
					FilteringSpot != null ? FilteringSpot.Item2 : null,
					FilteringTrack != null ? FilteringTrack.Item2 : null,
				   	FilteringSegment != null ? FilteringSegment.Item2 : null,
				   	null,
				   	null);
		}

	}
}
