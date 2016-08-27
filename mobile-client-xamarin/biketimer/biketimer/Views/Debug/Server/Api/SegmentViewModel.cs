using System;
using System.ComponentModel;

namespace Biketimer
{
	public class SegmentViewModel : INotifyPropertyChanged
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
					UpdateSegmentData();
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
					UpdateSegmentData();
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
					UpdateSegmentData();
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
					UpdateSegmentData();
				}
			}
			get
			{
				return _validTimeStop;
			}
		}

		private string _checkPointStartId;
		public string CheckPointStartId
		{
			set
			{
				if (_checkPointStartId != value)
				{
					_checkPointStartId = value;
					OnPropertyChanged("CheckPointStartId");
					UpdateSegmentData();
				}
			}
			get
			{
				return _checkPointStartId;
			}
		}

		private string _checkPointStartLatitude;
		public string CheckPointStartLatitude
		{
			set
			{
				if (_checkPointStartLatitude != value)
				{
					_checkPointStartLatitude = value;
					OnPropertyChanged("CheckPointStartLatitude");
					UpdateSegmentData();
				}
			}
			get
			{
				return _checkPointStartLatitude;
			}
		}

		private string _checkPointStartLongitude;
		public string CheckPointStartLongitude
		{
			set
			{
				if (_checkPointStartLongitude != value)
				{
					_checkPointStartLongitude = value;
					OnPropertyChanged("CheckPointStartLongitude");
					UpdateSegmentData();
				}
			}
			get
			{
				return _checkPointStartLongitude;
			}
		}

		private string _checkPointStopId;
		public string CheckPointStopId
		{
			set
			{
				if (_checkPointStopId != value)
				{
					_checkPointStopId = value;
					OnPropertyChanged("CheckPointStopId");
					UpdateSegmentData();
				}
			}
			get
			{
				return _checkPointStopId;
			}
		}

		private string _checkPointStopLatitude;
		public string CheckPointStopLatitude
		{
			set
			{
				if (_checkPointStopLatitude != value)
				{
					_checkPointStopLatitude = value;
					OnPropertyChanged("CheckPointStopLatitude");
					UpdateSegmentData();
				}
			}
			get
			{
				return _checkPointStopLatitude;
			}
		}

		private string _checkPointStopLongitude;
		public string CheckPointStopLongitude
		{
			set
			{
				if (_checkPointStopLongitude != value)
				{
					_checkPointStopLongitude = value;
					OnPropertyChanged("CheckPointStopLongitude");
					UpdateSegmentData();
				}
			}
			get
			{
				return _checkPointStopLongitude;
			}
		}

		public SegmentViewModel(Biketimer.BiketimerApiServer.Entities.Segment segment)
		{
			_id = segment.Id.ToString();
			_name = segment.Name;
			_validTimeStart = segment.ValidTimeStart.ToString();
			_validTimeStop = segment.ValidTimeStop != DateTime.MinValue
									? segment.ValidTimeStop.ToString()
									: "null";
			_checkPointStartId = segment.LocationStart.Id.ToString();
			_checkPointStartLatitude = segment.LocationStart.Location.La.ToString();
			_checkPointStartLongitude = segment.LocationStart.Location.Lo.ToString();
			_checkPointStopId = segment.LocationStop.Id.ToString();
			_checkPointStopLatitude = segment.LocationStop.Location.La.ToString();
			_checkPointStopLongitude = segment.LocationStop.Location.Lo.ToString();
		}

		protected virtual void OnPropertyChanged(string propertyName)
		{
			if (PropertyChanged != null)
			{
				PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
			}
		}

		private void UpdateSegmentData()
		{

		}
	}
}

