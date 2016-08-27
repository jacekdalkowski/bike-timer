using System;
using System.ComponentModel;

namespace Biketimer
{
	public class UserStatsPageModel : INotifyPropertyChanged
	{
		public event PropertyChangedEventHandler PropertyChanged;

		private string _filteringSpot;
		public string FilteringSpot
		{
			set
			{
				if (_filteringSpot != value)
				{
					_filteringSpot = value;
					OnPropertyChanged("FilteringSpot");
				}
			}
			get
			{
				return _filteringSpot;
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

