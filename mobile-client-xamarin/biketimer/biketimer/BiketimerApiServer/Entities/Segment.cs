using System;
using Newtonsoft.Json;

namespace Biketimer.BiketimerApiServer.Entities
{
	public class Segment
	{
		
		public Guid Id { get; set; }

		public string Name { get; set; }

		[JsonProperty(PropertyName = "location_start")]
		public Checkpoint LocationStart { get; set; }

		[JsonProperty(PropertyName = "location_stop")]
		public Checkpoint LocationStop { get; set; }

		[JsonProperty(PropertyName = "valid_time_start")]
		public DateTime ValidTimeStart { get; set; }

		[JsonProperty(PropertyName = "valid_time_stop")]
		public DateTime ValidTimeStop { get; set; }
	}
}

