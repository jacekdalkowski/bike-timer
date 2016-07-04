using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Biketimer.Facebook
{
	public abstract class FacebookStateManagerCommon
	{
		public event Action<FacebookAccount> LoginCompleted;
		public event Action LogoutCompleted;

		private FacebookAccount _facebookAccountData;
		private readonly FacebookFacade _facebookFacade;


		public FacebookStateManagerCommon()
		{
			_facebookFacade = new FacebookFacade();
		}

		public async Task OnAccessTokenReceived(FacebookAccess facebookAccessData)
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
		}
	}
}

