using System;
using System.Collections.Generic;

namespace Biketimer
{
	public class FacebookAccess
	{
		public string AccessToken { get; private set; }
		public IEnumerable<string> GrantedPermissions { get; private set; }

		public FacebookAccess(string accessToken, IEnumerable<string> grantedPermissions)
		{
			AccessToken = accessToken;
			GrantedPermissions = grantedPermissions;
		}
	}
}

