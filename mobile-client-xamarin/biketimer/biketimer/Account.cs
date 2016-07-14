using System;
namespace Biketimer
{
	public class Account
	{
		public FacebookAccount FacebookAccountData { get; private set; }

		public BiketimerAccount BiketimerAccountData { get; private set; }

		public Account(FacebookAccount facebookAccountData, BiketimerAccount biketimerAccountData)
		{
			FacebookAccountData = facebookAccountData;
			BiketimerAccountData = biketimerAccountData;
		}
	}
}

