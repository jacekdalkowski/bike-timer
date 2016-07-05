using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Biketimer.Facebook
{
	public abstract class FacebookStateManagerCommon
	{
		public event Action<FacebookAccount> LoginCompleted;
		public event Action LogoutCompleted;

		private readonly FacebookFacade _facebookFacade;
		private FacebookAccount _facebookAccountData;

		public FacebookAccount Account
		{
			get
			{
				return _facebookAccountData;
			}
		}


		public FacebookStateManagerCommon()
		{
			_facebookFacade = new FacebookFacade();
		}

		public void SetAccessToken(FacebookAccess facebookAccessData)
		{
			System.Threading.Tasks.Task.Run(async () => await SetAccessTokenAsync(facebookAccessData));

		}

		private async Task SetAccessTokenAsync(FacebookAccess facebookAccessData)
		{
			FacebookProfile profile = await _facebookFacade.GetUserProfile(facebookAccessData.AccessToken);
			_facebookAccountData = new FacebookAccount(facebookAccessData, profile);
			if (LoginCompleted != null)
			{
				LoginCompleted(_facebookAccountData);
			}
		}

		public void OnLoggedOut()
		{
			_facebookAccountData = null;
			if (LoginCompleted != null)
			{
				LogoutCompleted();
			}
		}
	}
}

