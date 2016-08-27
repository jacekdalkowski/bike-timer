using System;
using System.ComponentModel;
using Biketimer.BiketimerApiServer.Entities;

namespace Biketimer.Views.Debug.Server.Api
{
	public class SpotAndTracksViewModel : INotifyPropertyChanged
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
					UpdateSpotData();
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
					UpdateSpotData();
				}
			}
			get
			{
				return _name;
			}
		}

		private string _tags;
		public string Tags
		{
			set
			{
				if (_tags != value)
				{
					_tags = value;
					OnPropertyChanged("Tags");
					UpdateSpotData();
				}
			}
			get
			{
				return _tags;
			}
		}

		public SpotAndTracksViewModel(Spot spot)
		{
			_id = spot.Id.ToString();
			_name = spot.Name;
			_tags = string.Join("\n", spot.Tags);
		}

		protected virtual void OnPropertyChanged(string propertyName)
		{
			if (PropertyChanged != null)
			{
				PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
			}
		}

		private void UpdateSpotData()
		{

		}
	}
}

