using System;
using Biketimer.Account;

namespace Biketimer.LocalStorage
{
	public interface ILocalStorageManager
	{
		void SaveAccountData(AccountData accountData);
		AccountData GetAccountData();
	}
}

