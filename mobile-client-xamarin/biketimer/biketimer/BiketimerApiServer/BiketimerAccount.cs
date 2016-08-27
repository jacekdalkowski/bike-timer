using System;

namespace Biketimer.BiketimerApiServer
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

		public bool IsValid()
		{
			return Access != null && Access.IsValid()
				&& Profile != null && Profile.IsValid();
		}

		public override string ToString()
		{
			return string.Format("[BiketimerAccount: Access={0},\nProfile={1}]", Access, Profile);
		}
	}
}

