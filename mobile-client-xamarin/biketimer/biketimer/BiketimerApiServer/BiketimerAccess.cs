using System;
namespace Biketimer
{
	public class BiketimerAccess
	{
		public string AccessToken { get; set; }

		public BiketimerAccess(string accessToken)
		{
			AccessToken = accessToken;
		}

		public bool IsValid()
		{
			// TODO validate token expirtaion date
			return !string.IsNullOrEmpty(AccessToken);
		}

		public override string ToString()
		{
			return string.Format("[BiketimerAccess: AccessToken={0}]", AccessToken);
		}
	}
}

