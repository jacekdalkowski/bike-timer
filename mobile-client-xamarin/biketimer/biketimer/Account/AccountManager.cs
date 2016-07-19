using System;
using System.Threading.Tasks;

namespace Biketimer
{
	public class AccountManager
	{
		public event Action<Account> LoginCompleted;
		public event Action LoginFailed;
		public event Action LogoutCompleted;

		private Account _accountData;
		public Account AccountData
		{
			get
			{
				return _accountData;
			}
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

		public void RestoreAccountData(Account accountData)
		{
			_accountData = accountData;
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

