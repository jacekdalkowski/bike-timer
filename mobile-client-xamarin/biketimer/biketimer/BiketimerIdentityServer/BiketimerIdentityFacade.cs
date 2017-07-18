using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Biketimer
{
	public class BiketimerIdentityFacade
	{
		private const string _tokenEndpoint = "/token";
		private readonly string _identityDomainUrl;

		public BiketimerIdentityFacade(string identityDomainUrl)
		{
			this._identityDomainUrl = identityDomainUrl;
		}

		public async Task<BiketimerIdentityResponse> GetBiketimerToken(string facebookAccessToken)
		{
			using (var client = new HttpClient())
			{
				client.BaseAddress = new Uri(_identityDomainUrl);
				var content = new FormUrlEncodedContent(new[]
				{
					new KeyValuePair<string, string>("grantType", "facebook_token"),
					new KeyValuePair<string, string>("accessToken", facebookAccessToken)
				});

				var result = await client.PostAsync(_tokenEndpoint, content); // TODO may throw
				if (result.IsSuccessStatusCode && result.StatusCode == System.Net.HttpStatusCode.OK)
				{
					var rawResponse = await result.Content.ReadAsStringAsync();
					var identityResponse = await Task.Run(() => JsonConvert.DeserializeObject<BiketimerIdentityResponse>(rawResponse));
					return identityResponse;
				}
				else
				{
					throw new BiketimerIdentityException(); // TODO: some kind of identity-server-connection-exceptio 
				}
			}
		}
	}
}

