using System;
namespace Biketimer
{
	public class BiketimerAccess
	{
		public string AccessToken { get; private set; }

		public BiketimerAccess(string accessToken)
		{
			AccessToken = accessToken;
		}
	}
}

