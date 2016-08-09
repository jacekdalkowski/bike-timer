using System;
using Biketimer.Account;

namespace Biketimer
{
	public class AppDataViewModel
	{
		public string AccountData { get; set;}

		public AppDataViewModel(AccountData accountData)
		{
			AccountData = accountData != null ? accountData.ToString() : "null";
		}
	}
}

