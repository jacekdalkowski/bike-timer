using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace Biketimer
{
	public class BiketimerProfile
	{
		public string Id { get; set; }

		public string Email { get; set; }

		[JsonProperty(PropertyName = "bt_name")]
		public string BtName { get; set; }

		public IEnumerable<string> Roles { get; set; }

		public IEnumerable<string> Friends { get; set; }

		[JsonProperty(PropertyName = "fb_id")]
		public string FbId { get; set; }

		[JsonProperty(PropertyName = "fb_name")]
		public string FbName { get; set; }

		[JsonProperty(PropertyName = "fb_surname")]
		public string FbSurname { get; set; }

		public bool IsValid()
		{
			return !string.IsNullOrEmpty(Id);
		}

		public override string ToString()
		{
			return string.Format("[BiketimerProfile: Id={0},\nEmail={1},\nBtName={2},\nRoles=({3}),\nFriends=({4}),\nFbId={5},\nFbName={6},\nFbSurname={7}]", 
			        Id, Email, BtName, string.Join(", ", Roles), string.Join(", ", Friends), FbId, FbName, FbSurname);
		}
	}
}

