using System;
using System.Linq;
using System.Collections.Generic;
using Biketimer.BiketimerApiServer.Entities;

namespace Biketimer.Views.Stats.Common.Filtering
{
	public partial class FilteringModel
	{
		
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
	}
}
