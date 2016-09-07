using System;
using System.Threading.Tasks;

namespace Biketimer.Account
{
	public class AccountManager
	{
		public event Action<AccountData> LoginCompleted;
		public event Action LoginFailed;
		public event Action LogoutCompleted;

		private AccountData _accountData;
		public AccountData AccountData
		{
			get
			{
				return _accountData;
			}
		}

		public bool FacebookAccountDataPresent()
		{
			return AccountData != null
					&& AccountData.FacebookAccountData != null
					&& AccountData.FacebookAccountData.IsValid();
		}

		public bool BiketimerAccountDataPresent()
		{
			return AccountData != null
					&& AccountData.BiketimerAccountData != null
					&& AccountData.BiketimerAccountData.IsValid();
		}

		public void StartLogin(FacebookAccess facebookAccess)
		{
			Task.Run(async () => await HandleLoginProcessAsync(facebookAccess));
		}

		private async Task HandleLoginProcessAsync(FacebookAccess facebookAccess)
		{
			try
			{
				LoginProcessor loginProcessor = new LoginProcessor();
				_accountData = await loginProcessor.LoginAsync(facebookAccess);
				if (LoginCompleted != null)
				{
					LoginCompleted(_accountData);
				}
			}
			catch(Exception e)
			{
				if (LoginFailed != null)
				{
					LoginFailed();
				}
			}
		}

		public void RestoreAccountData(AccountData accountData)
		{
			_accountData = accountData;
			if (LoginCompleted != null)
			{
				LoginCompleted(_accountData);
			}
		}

		#region Singleton

		private AccountManager()
		{
		}

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

		#endregion
	}
}

