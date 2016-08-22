using System;
using System.ComponentModel;

namespace Biketimer.Views.Debug.Server.Api
{
	public class TrackAndSegmentsViewModel : INotifyPropertyChanged
	{
		public event PropertyChangedEventHandler PropertyChanged;

		private string _id;
		public string Id
		{
			set
			{
				if (_id != value)
				{
					_id = value;
					OnPropertyChanged("Id");
					UpdateTrackData();
				}
			}
			get
			{
				return _id;
			}
		}

		private string _name;
		public string Name
		{
			set
			{
				if (_name != value)
				{
					_name = value;
					OnPropertyChanged("Name");
					UpdateTrackData();
				}
			}
			get
			{
				return _name;
			}
		}

		private string _validTimeStart;
		public string ValidTimeStart
		{
			set
			{
				if (_validTimeStart != value)
				{
					_validTimeStart = value;
					OnPropertyChanged("ValidTimeStart");
					UpdateTrackData();
				}
			}
			get
			{
				return _validTimeStart;
			}
		}

		private string _validTimeStop;
		public string ValidTimeStop
		{
			set
			{
				if (_validTimeStop != value)
				{
					_validTimeStop = value;
					OnPropertyChanged("ValidTimeStop");
					UpdateTrackData();
				}
			}
			get
			{
				return _validTimeStop;
			}
		}

		public TrackAndSegmentsViewModel(Track track)
		{
			_id = track.Id.ToString();
			_name = track.Name;
			_validTimeStart = track.ValidTimeStart.ToString();
			_validTimeStop = track.ValidTimeStop.ToString();
		}

		protected virtual void OnPropertyChanged(string propertyName)
		{
			if (PropertyChanged != null)
			{
				PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
			}
		}

		private void UpdateTrackData()
		{

		}
	}
}

