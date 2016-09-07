using System;
using System.IO;
using Biketimer.Account;
using Newtonsoft.Json;

namespace Biketimer.iOS.LocalStorage
{
	public class LocalStorageManager : Biketimer.LocalStorage.ILocalStorageManager
	{
		public LocalStorageManager()
		{
		}

		public AccountData GetAccountData()
		{
			string myDocumentsPath = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
			string filePath = Path.Combine(myDocumentsPath, "accountData.json");

			bool fileExists = File.Exists(filePath);
			if (fileExists)
			{
				string jsonString = File.ReadAllText(filePath);
				AccountData accountData = JsonConvert.DeserializeObject<AccountData>(jsonString);
				return accountData;
			}
			else
			{
				return null;
			}
		}

		public void SaveAccountData(AccountData accountData)
		{
			string jsonString = JsonConvert.SerializeObject(accountData, Newtonsoft.Json.Formatting.Indented);

			string myDocumentsPath = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
			string filePath = Path.Combine(myDocumentsPath, "accountData.json");
			File.WriteAllText(filePath, jsonString);
		}
	}
}

