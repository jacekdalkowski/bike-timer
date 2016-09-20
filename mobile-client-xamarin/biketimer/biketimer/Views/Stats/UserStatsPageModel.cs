using System;
using System.Collections.Generic;
using System.ComponentModel;
using Biketimer.BiketimerApiServer.Entities;
using System.Linq;

namespace Biketimer
{
	public class UserStatsPageModel : INotifyPropertyChanged
	{
		public event PropertyChangedEventHandler PropertyChanged;

		private IEnumerable<Spot> _spotsData;

		private bool _isLoadingInitData;
		public bool IsLoadingInitData
		{
			set
			{
				if (_isLoadingInitData != value)
				{
					_isLoadingInitData = value;
					IsInitDataLoaded = !_isLoadingInitData;
					OnPropertyChanged("IsLoadingInitData");
				}
			}
			get
			{
				return _isLoadingInitData;
			}
		}

		public bool IsInitDataLoaded
		{
			set
			{
				OnPropertyChanged("IsInitDataLoaded");
			}
			get 
			{ 
				return !IsLoadingInitData; 
			}
		}

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
					IsFilteringSpotSet = _filteringSpot != null;
				}
			}
			get
			{
				return _filteringSpot;
			}
		}

		public bool IsFilteringSpotSet
		{
			set
			{
				OnPropertyChanged("IsFilteringSpotSet");
			}
			get
			{
				return _filteringSpot != null;
			}
		}

		private IEnumerable<Tuple<string, string>> _filteringTracksList;
		public IEnumerable<Tuple<string, string>> FilteringTracksList
		{
			private set
			{
				_filteringTracksList = value;
				OnPropertyChanged("FilteringTracksList");
			}
			get
			{
				return _filteringTracksList;
			}
		}

		private Tuple<string, string> _filteringTrack;
		public Tuple<string, string> FilteringTrack
		{
			set
			{
				if (!Tuple.Equals(_filteringTrack, value))
				{
					_filteringTrack = value;
					Track filteringTrack = _spotsData.Single(s => string.Equals(s.Id.ToString(), _filteringSpot.Item2, StringComparison.Ordinal))
					                                 .TracksCurrent
						                             .Single(t => string.Equals(t.Id.ToString(), _filteringTrack.Item2, StringComparison.Ordinal));
					FilteringSegmentsList = filteringTrack.SegmentsCurrent.Select(t => Tuple.Create(t.Name, t.Id.ToString()));
					OnPropertyChanged("FilteringTrack");
					IsFilteringTrackSet = _filteringTrack != null;
				}
			}
			get
			{
				return _filteringTrack;
			}
		}

		public bool IsFilteringTrackSet
		{
			set
			{
				OnPropertyChanged("IsFilteringTrackSet");
			}
			get
			{
				return _filteringTrack != null;
			}
		}

		private IEnumerable<Tuple<string, string>> _filteringSegmentsList;
		public IEnumerable<Tuple<string, string>> FilteringSegmentsList
		{
			private set
			{
				_filteringSegmentsList = value;
				OnPropertyChanged("FilteringSegmentsList");
			}
			get
			{
				return _filteringSegmentsList;
			}
		}

		private Tuple<string, string> _filteringSegment;
		public Tuple<string, string> FilteringSegment
		{
			set
			{
				if (!Tuple.Equals(_filteringSegment, value))
				{
					_filteringSegment = value;
					OnPropertyChanged("FilteringSegment");
					IsFilteringSegmentSet = _filteringSegment != null;
				}
			}
			get
			{
				return _filteringSegment;
			}
		}

		public bool IsFilteringSegmentSet
		{
			set
			{
				OnPropertyChanged("IsFilteringSegmentSet");
			}
			get
			{
				return _filteringSegment != null;
			}
		}

		protected virtual void OnPropertyChanged(string propertyName)
		{
			if (PropertyChanged != null)
			{
				PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
			}

		}
	}
}

