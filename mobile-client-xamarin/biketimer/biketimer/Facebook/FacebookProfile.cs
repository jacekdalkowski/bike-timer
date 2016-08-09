using System;
using Newtonsoft.Json;

namespace Biketimer
{
	public class FacebookProfile
	{
		public string Id { get; set; }

		public string Email { get; set; }

		[JsonProperty(PropertyName = "first_name")]
		public string FirstName { get; set; }

		[JsonProperty(PropertyName = "last_name")]
		public string LastName { get; set; }

		public string Name { get; set; }

		public string Gender { get; set; }

		public bool IsValid()
		{
			// TODO
			return true;
		}
	}
}

