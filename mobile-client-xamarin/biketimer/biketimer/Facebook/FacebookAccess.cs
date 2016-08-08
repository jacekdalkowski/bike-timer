using System;
using System.Collections.Generic;

namespace Biketimer
{
	public class FacebookAccess
	{
		public string AccessToken { get; set; }
		public IEnumerable<string> GrantedPermissions { get; set; }

		public FacebookAccess(string accessToken, IEnumerable<string> grantedPermissions)
		{
			AccessToken = accessToken;
			GrantedPermissions = grantedPermissions;
		}
	}
}

