using System;
using System.Threading.Tasks;
using Biketimer.BiketimerApiServer;

namespace Biketimer
{
	internal class LoginProcessor
	{
		private readonly FacebookFacade _facebookFacade;
		private readonly BiketimerIdentityFacade _biketimerIdentityFacade;
		private readonly BiketimerFacade _biketimerFacade;

		internal LoginProcessor()
		{
			_facebookFacade = new FacebookFacade();
			_biketimerIdentityFacade = new BiketimerIdentityFacade();
			_biketimerFacade = new BiketimerFacade();
		}

		public async Task<Account> LoginAsync(FacebookAccess facebookAccess)
		{
			Task<FacebookProfile> facebookProfileTask = _facebookFacade.GetUserProfile(facebookAccess.AccessToken);

			Task<BiketimerAccount> biketimerAccountTask = _biketimerIdentityFacade.GetBiketimerToken(facebookAccess.AccessToken)
															   .ContinueWith(DownloadBiketimerAccountAsync)
															   .Unwrap();

			FacebookProfile facebookProfile = await facebookProfileTask;
			BiketimerAccount biketimerAccount = await biketimerAccountTask;

			FacebookAccount facebookAccount = new FacebookAccount(facebookAccess, facebookProfile);
			Account _accountData = new Account(facebookAccount, biketimerAccount);

			return _accountData;
		}

		private async Task<BiketimerAccount> DownloadBiketimerAccountAsync(Task<BiketimerIdentityResponse> identityResponse)
		{
			if (identityResponse.Result == null)
			{
				return null;
			}

			var biketimerAccessToken = identityResponse.Result.Token;
			var biketimerProfile = await _biketimerFacade.GetUserProfile(biketimerAccessToken);
			var biketimerAccess = new BiketimerAccess(biketimerAccessToken);
			var biketimerAccount = new BiketimerAccount(biketimerAccess, biketimerProfile);
			return biketimerAccount;
		}
	}
}

