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
			_filteringSpotsNamesList = spotsData.Select(s => s.Name);
		}

		private IEnumerable<string> _filteringSpotsNamesList;
		public IEnumerable<string> FilteringSpotsNamesList
		{
			private set
			{
				_filteringSpotsNamesList = value;
				OnPropertyChanged("FilteringSpotsNamesList");
			}
			get
			{
				return _filteringSpotsNamesList;
			}
		}

		private string _filteringSpotName;
		public string FilteringSpotName
		{
			set
			{
				if (_filteringSpotName != value)
				{
					_filteringSpotName = value;
					Spot filteringSpot = _spotsData.Single(s => string.Equals(s.Name, _filteringSpotName, StringComparison.Ordinal));
					FilteringTracksNamesList = filteringSpot.TracksCurrent.Select(t => t.Name);
					OnPropertyChanged("FilteringSpotName");
					IsFilteringSpotNameSet = !string.IsNullOrEmpty(_filteringSpotName);
				}
			}
			get
			{
				return _filteringSpotName;
			}
		}

		public bool IsFilteringSpotNameSet
		{
			set
			{
				OnPropertyChanged("IsFilteringSpotNameSet");
			}
			get
			{
				return !string.IsNullOrEmpty(_filteringSpotName);
			}
		}

		private IEnumerable<string> _filteringTracksNamesList;
		public IEnumerable<string> FilteringTracksNamesList
		{
			private set
			{
				_filteringTracksNamesList = value;
				OnPropertyChanged("FilteringTracksNamesList");
			}
			get
			{
				return _filteringTracksNamesList;
			}
		}

		private string _filteringTrackName;
		public string FilteringTrackName
		{
			set
			{
				if (_filteringTrackName != value)
				{
					_filteringTrackName = value;
					Track filteringTrack = _spotsData.Single(s => string.Equals(s.Name, _filteringSpotName, StringComparison.Ordinal))
					                                 .TracksCurrent
					                                 .Single(t => string.Equals(t.Name, _filteringTrackName, StringComparison.Ordinal));
					FilteringSegmentsNamesList = filteringTrack.SegmentsCurrent.Select(t => t.Name);
					OnPropertyChanged("FilteringTrackName");
					IsFilteringTrackNameSet = !string.IsNullOrEmpty(_filteringTrackName);
				}
			}
			get
			{
				return _filteringTrackName;
			}
		}

		public bool IsFilteringTrackNameSet
		{
			set
			{
				OnPropertyChanged("IsFilteringTrackNameSet");
			}
			get
			{
				return !string.IsNullOrEmpty(_filteringTrackName);
			}
		}

		private IEnumerable<string> _filteringSegmentsNamesList;
		public IEnumerable<string> FilteringSegmentsNamesList
		{
			private set
			{
				_filteringSegmentsNamesList = value;
				OnPropertyChanged("FilteringSegmentsNamesList");
			}
			get
			{
				return _filteringSegmentsNamesList;
			}
		}

		private string _filteringSegmentName;
		public string FilteringSegmentName
		{
			set
			{
				if (_filteringSegmentName != value)
				{
					_filteringSegmentName = value;
					OnPropertyChanged("FilteringSegmentName");
					IsFilteringSegmentNameSet = !string.IsNullOrEmpty(_filteringSegmentName);
				}
			}
			get
			{
				return _filteringSegmentName;
			}
		}

		public bool IsFilteringSegmentNameSet
		{
			set
			{
				OnPropertyChanged("IsFilteringSegmentNameSet");
			}
			get
			{
				return !string.IsNullOrEmpty(_filteringSegmentName);
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

