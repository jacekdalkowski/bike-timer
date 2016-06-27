using System;
using System.Collections.Generic;

namespace Biketimer
{
	public class FacebookAccount
	{
		public FacebookAccess Access { get; private set; }
		public FacebookProfile Profile { get; private set; }

		public FacebookAccount(FacebookAccess access, FacebookProfile profile)
		{
			Access = access;
			Profile = profile;
		}
	}
}

