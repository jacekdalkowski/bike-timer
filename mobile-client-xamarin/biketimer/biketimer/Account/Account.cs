using System;

namespace Biketimer.Account
{
	public class AccountData
	{
		public FacebookAccount FacebookAccountData { get; private set; }
		public BiketimerAccount BiketimerAccountData { get; private set; }

		public AccountData(FacebookAccount facebookAccountData, BiketimerAccount biketimerAccountData)
		{
			FacebookAccountData = facebookAccountData;
			BiketimerAccountData = biketimerAccountData;
		}

		public override string ToString()
		{
			return string.Format("[AccountData: FacebookAccountData={0},\n\nBiketimerAccountData={1}]", 
			                     FacebookAccountData, BiketimerAccountData);
		}
	}
}

