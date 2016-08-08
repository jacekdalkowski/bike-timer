using System;
using System.Collections.Generic;
using Xamarin.Forms;
using Biketimer.BiketimerApiServer;
using System.Threading.Tasks;

namespace Biketimer.Views.Debug.Server.Api
{
	public partial class Spots : ContentPage
	{
		public Spots()
		{
			InitializeComponent();

			if (AccountManager.Instance.AccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData.Access != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData.Access.AccessToken != null)
			{
				BiketimerFacade biketimerFacade = new BiketimerFacade();
				biketimerFacade.GetSpots(AccountManager.Instance.AccountData.BiketimerAccountData.Access.AccessToken)
							   .ContinueWith(OnSpotsDownloaded);
			}
		}

		private void OnSpotsDownloaded(Task<IEnumerable<Spot>> spotsTask)
		{
			IEnumerable<Spot> spots = spotsTask.Result;
			BindingContext = spots;
		}
	}
}

