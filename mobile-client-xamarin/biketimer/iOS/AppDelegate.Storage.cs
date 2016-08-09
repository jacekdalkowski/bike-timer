using System;
using Biketimer.Account;

namespace Biketimer.iOS
{
	public partial class AppDelegate
	{
		private const string AccountDataKey = "accountData";

		private void SaveAccountData(AccountData accountData)
		{
			_formsApp.Properties[AccountDataKey] = accountData;
		}

		private AccountData GetAccountData()
		{
			if (_formsApp.Properties.ContainsKey(AccountDataKey))
			{
				return _formsApp.Properties[AccountDataKey] as AccountData;
			}

			return null;
		}
	}
}

