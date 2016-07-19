using System;
namespace Biketimer
{
	public class BiketimerIdentityException : Exception
	{
		public BiketimerIdentityException()
		{
		}

		public BiketimerIdentityException(string message)
	        : base(message)
	    {
		}

		public BiketimerIdentityException(string message, Exception inner)
	        : base(message, inner)
	    {
		}
	}
}

