using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;

namespace Biketimer
{
	public class FacebookAccountDebugPageViewModel : INotifyPropertyChanged
	{
		public event PropertyChangedEventHandler PropertyChanged;

		#region Facebook access

		private string _accessToken;
		public string AccessToken 
		{ 
			set
			{
				if (_accessToken != value)
				{
					_accessToken = value;
					OnPropertyChanged("AccessToken");
					UpdateFacebookAccountData();
				}
			}
			get
			{
				return _accessToken;
			} 
		}

		private string _grantedPermissions;
		public string GrantedPermissions 
		{ 
			set
			{
				if (_grantedPermissions != value)
				{
					_grantedPermissions = value;
					OnPropertyChanged("GrantedPermissions");
					UpdateFacebookAccountData();
				}
			}
			get
			{
				return _grantedPermissions;
			}
		}

		#endregion

		#region Facebook profile

		private string _id;
		public string Id 
		{ 
			set
			{
				if (_id != value)
				{
					_id = value;
					OnPropertyChanged("Id");
					UpdateFacebookAccountData();
				}
			}
			get
			{
				return _id;
			}
		}

		private string _email;
		public string Email 
		{ 
			set
			{
				if (_email != value)
				{
					_email = value;
					OnPropertyChanged("Email");
					UpdateFacebookAccountData();
				}
			}
			get
			{
				return _email;
			}
		}

		private string _firstName;
		public string FirstName 
		{
			set
			{
				if (_firstName != value)
				{
					_firstName = value;
					OnPropertyChanged("FirstName");
					UpdateFacebookAccountData();
				}
			}
			get
			{
				return _firstName;
			}
		}

		private string _lastName;
		public string LastName 
		{ 
			set
			{
				if (_lastName != value)
				{
					_lastName = value;
					OnPropertyChanged("LastName");
					UpdateFacebookAccountData();
				}
			}
			get
			{
				return _lastName;
			}
		}

		private string _name;
		public string Name 
		{ 
			set
			{
				if (_name != value)
				{
					_name = value;
					OnPropertyChanged("Name");
					UpdateFacebookAccountData();
				}
			}
			get
			{
				return _name;
			}
		}

		private string _gender;
		public string Gender 
		{ 
			set
			{
				if (_gender != value)
				{
					_gender = value;
					OnPropertyChanged("Gender");
					UpdateFacebookAccountData();
				}
			}
			get
			{
				return _gender;
			}
		}

		#endregion

		protected virtual void OnPropertyChanged(string propertyName)
		{
			if (PropertyChanged != null)
			{
				PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
			}
		}

		public FacebookAccountDebugPageViewModel()
		{
			if (AccountManager.Instance != null
					&& AccountManager.Instance.AccountData != null
			    	&& AccountManager.Instance.AccountData.FacebookAccountData != null
					&& AccountManager.Instance.AccountData.FacebookAccountData.Access != null)
			{
				var facebookAccountAccessData = AccountManager.Instance.AccountData.FacebookAccountData.Access;
				_accessToken = facebookAccountAccessData.AccessToken;
				if (facebookAccountAccessData.GrantedPermissions != null)
				{
					_grantedPermissions = string.Join("\n", facebookAccountAccessData.GrantedPermissions);
				}
			}

			if (AccountManager.Instance != null
					&& AccountManager.Instance.AccountData != null
					&& AccountManager.Instance.AccountData.FacebookAccountData != null
			    	&& AccountManager.Instance.AccountData.FacebookAccountData.Profile != null)
			{
				var facebookAccountProfileData = AccountManager.Instance.AccountData.FacebookAccountData.Profile;
				_id = facebookAccountProfileData.Id;
				_email = facebookAccountProfileData.Email;
				_firstName = facebookAccountProfileData.FirstName;
				_lastName = facebookAccountProfileData.LastName;
				_name = facebookAccountProfileData.Name;
				_gender = facebookAccountProfileData.Gender;
			}
		}

		private void UpdateFacebookAccountData()
		{
			// TODO: manager should return immutable copies of data and be updated by ummutalbe copies of data

			if (AccountManager.Instance != null
					&& AccountManager.Instance.AccountData != null
					&& AccountManager.Instance.AccountData.FacebookAccountData != null
			    	&& AccountManager.Instance.AccountData.FacebookAccountData.Access != null)
			{
				var facebookAccountAccessData = AccountManager.Instance.AccountData.FacebookAccountData.Access;
				facebookAccountAccessData.AccessToken = AccessToken;
				if (!string.IsNullOrEmpty(GrantedPermissions))
				{
					facebookAccountAccessData.GrantedPermissions = GrantedPermissions.Split('\n').AsEnumerable();
				}
				else
				{
					facebookAccountAccessData.GrantedPermissions = new string[0];
				}

			}

			if (AccountManager.Instance != null
					&& AccountManager.Instance.AccountData != null
					&& AccountManager.Instance.AccountData.FacebookAccountData != null
					&& AccountManager.Instance.AccountData.FacebookAccountData.Profile != null)
			{
				var facebookAccountProfileData = AccountManager.Instance.AccountData.FacebookAccountData.Profile;
				facebookAccountProfileData.Id = Id;
				facebookAccountProfileData.Email = Email;
				facebookAccountProfileData.FirstName = FirstName;
				facebookAccountProfileData.LastName = LastName;
				facebookAccountProfileData.Name = Name;
				facebookAccountProfileData.Gender = Gender;
			}
		}
	}
}

