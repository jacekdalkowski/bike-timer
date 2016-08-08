using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;

namespace Biketimer
{
	public class BiketimerAccountDebugPageViewModel : INotifyPropertyChanged
	{

		public event PropertyChangedEventHandler PropertyChanged;

		#region Biketimer access

		private string _accessToken;
		public string AccessToken
		{
			set
			{
				if (_accessToken != value)
				{
					_accessToken = value;
					OnPropertyChanged("AccessToken");
					UpdateBiketimerAccountData();
				}
			}
			get
			{
				return _accessToken;
			}
		}

		#endregion

		#region Biketimer profile 

		private string _id;
		public string Id
		{
			set
			{
				if (_id != value)
				{
					_id = value;
					OnPropertyChanged("Id");
					UpdateBiketimerAccountData();
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
					UpdateBiketimerAccountData();
				}
			}
			get
			{
				return _email;
			}
		}

		private string _btName;
		public string BtName
		{
			set
			{
				if (_btName != value)
				{
					_btName = value;
					OnPropertyChanged("BtName");
					UpdateBiketimerAccountData();
				}
			}
			get
			{
				return _btName;
			}
		}

		private string _fbId;
		public string FbId
		{
			set
			{
				if (_fbId != value)
				{
					_fbId = value;
					OnPropertyChanged("FbId");
					UpdateBiketimerAccountData();
				}
			}
			get
			{
				return _fbId;
			}
		}

		private string _fbName;
		public string FbName
		{
			set
			{
				if (_fbName != value)
				{
					_fbName = value;
					OnPropertyChanged("FbName");
					UpdateBiketimerAccountData();
				}
			}
			get
			{
				return _fbName;
			}
		}

		private string _fbSurname;
		public string FbSurname
		{
			set
			{
				if (_fbSurname != value)
				{
					_fbSurname = value;
					OnPropertyChanged("FbSurname");
					UpdateBiketimerAccountData();
				}
			}
			get
			{
				return _fbSurname;
			}
		}

		private string _roles;
		public string Roles
		{
			set
			{
				if (_roles != value)
				{
					_roles = value;
					OnPropertyChanged("Roles");
					UpdateBiketimerAccountData();
				}
			}
			get
			{
				return _roles;
			}
		}

		private string _friends;
		public string Friends
		{
			set
			{
				if (_friends != value)
				{
					_friends = value;
					OnPropertyChanged("Friends");
					UpdateBiketimerAccountData();
				}
			}
			get
			{
				return _friends;
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

		public BiketimerAccountDebugPageViewModel()
		{
			if (AccountManager.Instance != null
					&& AccountManager.Instance.AccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData != null
			    	&& AccountManager.Instance.AccountData.BiketimerAccountData.Access != null)
			{
				var biketimerAccountAccessData = AccountManager.Instance.AccountData.BiketimerAccountData.Access;
				_accessToken = biketimerAccountAccessData.AccessToken;
			}

			if (AccountManager.Instance != null
					&& AccountManager.Instance.AccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData.Profile != null)
			{
				var biketimerAccountProfileData = AccountManager.Instance.AccountData.BiketimerAccountData.Profile;
				_id = biketimerAccountProfileData.Id;
				_email = biketimerAccountProfileData.Email;
				_btName = biketimerAccountProfileData.BtName;
				_fbId = biketimerAccountProfileData.FbId;
				_fbName = biketimerAccountProfileData.FbName;
				_fbSurname = biketimerAccountProfileData.FbSurname;
				if (biketimerAccountProfileData.Roles != null)
				{
					_roles = string.Join("\n", biketimerAccountProfileData.Roles);
				}
				if (biketimerAccountProfileData.Friends != null)
				{
					_friends = string.Join("\n", biketimerAccountProfileData.Friends);
				}
			}
		}

		private void UpdateBiketimerAccountData()
		{
			// TODO: manager should return immutable compies of data and be updated by ummutalbe copies of data

			if (AccountManager.Instance != null
					&& AccountManager.Instance.AccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData != null
					&& AccountManager.Instance.AccountData.BiketimerAccountData.Access != null)
			{
				var biketimerAccountAccessData = AccountManager.Instance.AccountData.BiketimerAccountData.Access;
				biketimerAccountAccessData.AccessToken = AccessToken;
			}

			if (AccountManager.Instance != null 
				    && AccountManager.Instance.AccountData != null
				    && AccountManager.Instance.AccountData.BiketimerAccountData != null
			    	&& AccountManager.Instance.AccountData.BiketimerAccountData.Profile != null)
			{
				var biketimerAccountProfileData = AccountManager.Instance.AccountData.BiketimerAccountData.Profile;
				biketimerAccountProfileData.Id = Id;
				biketimerAccountProfileData.Email = Email;
				biketimerAccountProfileData.BtName = BtName;
				biketimerAccountProfileData.FbId = FbId;
				biketimerAccountProfileData.FbName = FbName;
				biketimerAccountProfileData.FbSurname = FbSurname;
				if (!string.IsNullOrEmpty(Roles))
				{
					biketimerAccountProfileData.Roles = Roles.Split('\n').AsEnumerable();
				}
				else 
				{
					biketimerAccountProfileData.Roles = new string[0];
				}

				if (!string.IsNullOrEmpty(Friends))
				{
					biketimerAccountProfileData.Friends = Friends.Split('\n').AsEnumerable();
				}
				else
				{
					biketimerAccountProfileData.Friends = new string[0];
				}
			}
		}
	}
}

