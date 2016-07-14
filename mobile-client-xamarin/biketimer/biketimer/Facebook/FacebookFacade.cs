using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace Biketimer
{
	public class FacebookFacade
	{
		private const string _facebookApiDomainUrl = "https://graph.facebook.com";
		private const string _getProfileAbsoluteUrl = "/v2.6/me?fields=id,email,first_name,last_name,name,gender";

		public async Task<FacebookProfile> GetUserProfile(string userAccessToken)
		{
			FacebookProfile profile = await GetData<FacebookProfile>(_getProfileAbsoluteUrl + "&access_token=" + userAccessToken);
			return profile;
		}

		private async Task<T> GetData<T>(string resourceUrl)
		{
			using (var client = new HttpClient())
			{
				client.BaseAddress = new Uri(_facebookApiDomainUrl);
				var result = await client.GetAsync(resourceUrl);
				if (result.IsSuccessStatusCode && result.StatusCode == System.Net.HttpStatusCode.OK)
				{
					//ok to process
					var rawResponse = await result.Content.ReadAsStringAsync();
					T parsedResponse = await Task.Run(() => JsonConvert.DeserializeObject<T>(rawResponse));
					return parsedResponse;
				}
				else
				{
					return default(T);
				}
			}
		}
	}
}

