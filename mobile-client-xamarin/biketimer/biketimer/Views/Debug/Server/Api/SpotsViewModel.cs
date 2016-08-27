using System;
using System.Collections.Generic;
using System.ComponentModel;
using Biketimer.BiketimerApiServer.Entities;

namespace Biketimer
{
	public class SpotsViewModel : INotifyPropertyChanged
	{
		public event PropertyChangedEventHandler PropertyChanged;

		private bool _isBusy;
		public bool IsBusy
		{
			get { return _isBusy; }
			set
			{
				_isBusy = value;
				OnPropertyChanged("IsBusy");
			}
		}

		private IEnumerable<Spot> _spots;
		public IEnumerable<Spot> Spots
		{
			get { return _spots; }
			set
			{
				_spots = value;
				OnPropertyChanged("Spots");
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

