using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Biketimer.Facebook
{
	public abstract class FacebookStateManagerCommon
	{
		public FacebookAccount FacebookAccountData { get; private set; }

		private readonly FacebookFacade _facebookFacade;

		public FacebookStateManagerCommon()
		{
			_facebookFacade = new FacebookFacade();
		}

		public async Task OnAccessTokenReceived(FacebookAccess facebookAccessData, Action<FacebookAccount> onLoginCompleted)
		{
			FacebookProfile profile = await _facebookFacade.GetUserProfile(facebookAccessData.AccessToken);
			FacebookAccountData = new FacebookAccount(facebookAccessData, profile);
			onLoginCompleted(FacebookAccountData);
		}

		public void OnLoggedOut()
		{
			FacebookAccountData = null;
		}
	}
}

