using System;
using System.Collections.Generic;
using System.ComponentModel;
using Biketimer.BiketimerApiServer.Entities;
using System.Linq;

namespace Biketimer.Views.Stats.Tabs.User
{
	public class UserStatsPageModel : INotifyPropertyChanged
	{
		public event PropertyChangedEventHandler PropertyChanged;



		public void Load()
		{

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

