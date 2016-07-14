using System;
namespace Biketimer
{
	public class BiketimerAccount
	{
		public BiketimerAccess Access { get; private set; }
		public BiketimerProfile Profile { get; private set; }

		public BiketimerAccount(BiketimerAccess access, BiketimerProfile profile)
		{
			Access = access;
			Profile = profile;
		}
	}
}

