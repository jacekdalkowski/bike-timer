using System;
using System.Collections.Generic;

namespace Biketimer
{
	public class BiketimerProfile
	{
		public string Id { get; set; }
		public string Email { get; set; }
		public string BtName { get; set; }
		public IEnumerable<string> Roles { get; set; }
		public IEnumerable<string> Friends { get; set; }

		public string FbId { get; set; }
		public string FbName { get; set; }
		public string FbSurname { get; set; }
	}
}

