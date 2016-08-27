using System;

namespace Biketimer.BiketimerApiServer.Entities
{
	public class Checkpoint
	{
		public Guid Id { get; set; }
		public GeoPoint Location { get; set; }
	}
}

