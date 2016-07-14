using System;
using System.Threading.Tasks;

namespace Biketimer
{
	public partial class AccountManager
	{
		private readonly FacebookFacade _facebookFacade;
		private readonly BiketimerIdentityFacade _biketimerIdentityFacade;
		private readonly BiketimerFacade _biketimerFacade;

		public event Action<Account> LoginCompleted;
		public event Action LoginFailed;
		public event Action LogoutCompleted;

		private Account _accountData;
		public Account AccountData
		{
			get
			{
				return _accountData;
			}
		}

		private AccountManager()
		{
			_facebookFacade = new FacebookFacade();
			_biketimerIdentityFacade = new BiketimerIdentityFacade();
			_biketimerFacade = new BiketimerFacade();
		}

		public async Task Login(FacebookAccess facebookAccess)
		{
			var facebookProfileTask = _facebookFacade.GetUserProfile(facebookAccess.AccessToken);

			var biketimerAccountTask = _biketimerIdentityFacade.GetBiketimerToken(facebookAccess.AccessToken)
															   .ContinueWith(async (bir) =>
															   	{
																	   if (bir.Result == null)
																		{
																		   return null;
																		}

																	   var biketimerAccessToken = bir.Result.Token;
																	   var biketimerProfile = await _biketimerFacade.GetUserProfile(biketimerAccessToken);
																	   var biketimerAccess = new BiketimerAccess(biketimerAccessToken);
																	   var biketimerAccount = new BiketimerAccount(biketimerAccess, biketimerProfile);
																	   return biketimerAccount;
																   })
															   .Unwrap();

			var facebookProfile = await facebookProfileTask;
			var biketimerAccount2 = await biketimerAccountTask;

			if (facebookProfile == null || biketimerAccount2 == null)
			{
				if (LoginFailed != null)
				{
					LoginFailed();
				}
				return;
			}

			FacebookAccount facebookAccount = new FacebookAccount(facebookAccess, facebookProfile);
			_accountData = new Account(facebookAccount, biketimerAccount2);
			if (LoginCompleted != null)
			{
				LoginCompleted(_accountData);
			}
		}
	}
}

