using System;
using System.Collections.Generic;

namespace Biketimer.Views.Stats.Common.Filtering
{
	public partial class FilteringModel
	{
		
		public IEnumerable<Tuple<string, string>> SortingOptionsList
		{
			get
			{
				return new List<Tuple<string, string>>()
				{
					Tuple.Create<string, string>("Time", "time"),
					Tuple.Create<string, string>("Date ascending", "date_asc"),
					Tuple.Create<string, string>("Date descending", "date_desc"),
				};
			}
		}

		private Tuple<string, string> _sortingOption;
		public Tuple<string, string> SortingOption
		{
			set
			{
				if (!Tuple.Equals(_sortingOption, value))
				{
					_sortingOption = value;
					OnPropertyChanged("SortingOption");
					IsSortingOptionSet = _sortingOption != null;
				}
			}
			get
			{
				return _sortingOption;
			}
		}

		public bool IsSortingOptionSet
		{
			set
			{
				OnPropertyChanged("IsSortingOptionSet");
			}
			get
			{
				return _sortingOption != null;
			}
		}

	}
}
