using System;

namespace Biketimer.iOS
{
	public partial class AppDelegate
	{
		private void SaveAccountData(Account accountData)
		{
			_formsApp.Properties["accountData"] = accountData;
		}

		private Account GetAccountData()
		{
			if (_formsApp.Properties.ContainsKey("accountData"))
			{
				return _formsApp.Properties["accountData"] as Account;
			}

			return null;
		}
	}
}

