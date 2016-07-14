using System;

namespace Biketimer
{
	public partial class AccountManager
	{
		private static AccountManager _instance = null;
		private static object _instanceLock = new object();

		public static AccountManager Instance
		{
			get
			{
				if (_instance == null)
				{
					lock (_instanceLock)
					{
						if (_instance == null)
							_instance = new AccountManager();
					}
				}

				return _instance;
			}
		}
	}
}

