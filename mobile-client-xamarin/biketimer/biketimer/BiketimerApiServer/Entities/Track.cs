using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace Biketimer.BiketimerApiServer.Entities
{
	public class Track
	{
		public Guid Id { get; set; }

		public string Name { get; set; }

		[JsonProperty(PropertyName = "segments_old")]
		public IEnumerable<Segment> SegmentsOld { get; set; }

		[JsonProperty(PropertyName = "segments_current")]
		public IEnumerable<Segment> SegmentsCurrent { get; set; }

		[JsonProperty(PropertyName = "valid_time_start")]
		public DateTime ValidTimeStart { get; set; }

		[JsonProperty(PropertyName = "valid_time_stop")]
		public DateTime? ValidTimeStop { get; set; }
	}
}

