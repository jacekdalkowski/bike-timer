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
	}
}

