using System;
namespace Biketimer
{
	public class BiketimerStateManager
	{
		public event Action<FacebookAccount> LoginCompleted;
		public event Action LogoutCompleted;

		private readonly BiketimerFacade _biketimerFacade;
		private BiketimerAccount _biketimerAccountData;

		public BiketimerAccount Account
		{
			get
			{
				return _biketimerAccountData;
			}
		}


		public BiketimerStateManager()
		{
			_biketimerFacade = new BiketimerFacade();
		}

		public void SetAccessToken(BiketimerAccount biketimerAccountData)
		{
			System.Threading.Tasks.Task.Run(async () => await SetAccessTokenAsync(biketimerAccountData));
		}

		private async Task SetAccessTokenAsync(BiketimerAccess biketimerAccessData)
		{
			BiketimerProfile profile = await _biketimerFacade.GetUserProfile(biketimerAccessData.AccessToken);
			_biketimerAccountData = new BiketimerAccount(biketimerAccessData, profile);
			if (LoginCompleted != null)
			{
				LoginCompleted(_biketimerAccountData);
			}
		}

		public void OnLoggedOut()
		{
			_biketimerAccountData = null;
			if (LoginCompleted != null)
			{
				LogoutCompleted();
			}
		}
	}
}

