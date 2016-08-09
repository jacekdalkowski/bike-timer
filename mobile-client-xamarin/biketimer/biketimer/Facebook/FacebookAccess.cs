using System;
using System.Linq;
using System.Collections.Generic;

namespace Biketimer
{
	public class FacebookAccess
	{
		public static readonly IEnumerable<string> RequiredPermissions = new string[] { "public_profile", "email" };
		public string AccessToken { get; set; }
		public IEnumerable<string> GrantedPermissions { get; set; }

		public FacebookAccess(string accessToken, IEnumerable<string> grantedPermissions)
		{
			AccessToken = accessToken;
			GrantedPermissions = grantedPermissions;
		}

		public bool IsValid()
		{
			// TODO: check expiration date
			bool accessTokenValid = !string.IsNullOrEmpty(AccessToken);

			bool permissionsValid = true;
			foreach (string requiredPermission in RequiredPermissions)
			{
				permissionsValid &= GrantedPermissions.Any(p => p == requiredPermission);
			}

			return accessTokenValid && permissionsValid;
		}
	}
}

