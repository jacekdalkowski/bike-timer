using System;
namespace Biketimer
{
	public interface IFacebookFacade
	{
		FacebookProfile GetUserProfile(string accessToken);
	}
}

