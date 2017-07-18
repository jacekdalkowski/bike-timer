using System;
using System.Linq;
using System.Collections.Generic;
using Biketimer.BiketimerApiServer.Entities;

namespace Biketimer.Views.Stats.Common.Filtering
{
	public partial class FilteringModel
	{

		public void SetSpotsData(IEnumerable<Spot> spotsData)
		{
			_spotsData = spotsData;
			_filteringSpotsList = spotsData.Select(s => Tuple.Create(s.Name, s.Id.ToString()));
		}

		private IEnumerable<Tuple<string, string>> _filteringSpotsList;
		public IEnumerable<Tuple<string, string>> FilteringSpotsList
		{
			private set
			{
				_filteringSpotsList = value;
				OnPropertyChanged("FilteringSpotsList");
			}
			get
			{
				return _filteringSpotsList;
			}
		}

		private Tuple<string, string> _filteringSpot;
		public Tuple<string, string> FilteringSpot
		{
			set
			{
				if (!Tuple.Equals(_filteringSpot, value))
				{
					_filteringSpot = value;
					Spot filteringSpot = _spotsData.Single(s => string.Equals(s.Id.ToString(), _filteringSpot.Item2, StringComparison.Ordinal));
					FilteringTracksList = filteringSpot.TracksCurrent.Select(t => Tuple.Create(t.Name, t.Id.ToString()));
					OnPropertyChanged("FilteringSpot");
					OnFilteringChanged();
				}
			}
			get
			{
				return _filteringSpot;
			}
		}

		public bool IsFilteringSpotSet
		{
			get
			{
				return _filteringSpot != null;
			}
		}
	}
}
