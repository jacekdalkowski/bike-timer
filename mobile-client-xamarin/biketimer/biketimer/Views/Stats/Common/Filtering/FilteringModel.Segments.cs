using System;
using System.Collections.Generic;

namespace Biketimer.Views.Stats.Common.Filtering
{
	public partial class FilteringModel
	{
		
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
	}
}
