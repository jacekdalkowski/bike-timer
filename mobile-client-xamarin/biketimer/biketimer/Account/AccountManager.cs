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

		private LoginProcessor _loginProcessor;

		public void StartLogin(FacebookAccess facebookAccess)
		{
			Task.Run(async () => await HandleLoginProcessAsync(facebookAccess));
		}

		private async Task HandleLoginProcessAsync(FacebookAccess facebookAccess)
		{
			try
			{
				LoginProcessor loginProcessor = new LoginProcessor();
				Account userAccount = await loginProcessor.LoginAsync(facebookAccess);
				if (LoginCompleted != null)
				{
					LoginCompleted(userAccount);
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

		#region Singleton

		private AccountManager()
		{
			_loginProcessor = new LoginProcessor();
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

