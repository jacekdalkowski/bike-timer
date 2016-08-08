using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace Biketimer
{
	public class Spot
	{
		public Guid Id { get; set; }

		public string Name { get; set; }

		public IEnumerable<string> Tags { get; set; }

		[JsonProperty(PropertyName = "tracks_old")]
		public IEnumerable<Track> TracksOld { get; set; }

		[JsonProperty(PropertyName = "tracks_current")]
		public IEnumerable<Track> TracksCurrent { get; set; }
	}
}

