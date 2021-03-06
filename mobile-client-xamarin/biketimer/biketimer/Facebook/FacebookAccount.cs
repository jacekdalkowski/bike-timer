﻿using System;
using System.Collections.Generic;

namespace Biketimer
{
	public class FacebookAccount
	{
		public FacebookAccess Access { get; private set; }
		public FacebookProfile Profile { get; private set; }

		public FacebookAccount(FacebookAccess access, FacebookProfile profile)
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
			return string.Format("[FacebookAccount: Access={0},\nProfile={1}]", Access, Profile);
		}
	}
}

