using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Biketimer.BiketimerApiServer
{
	public class BiketimerFacade
	{
		private const string _biketimerApiDomainUrl = "http://46.101.148.70:5001";
		private const string _getProfileAbsoluteUrl = "/User/Me";
		private const string _getSpotsAbsoluteUrl = "/Spots";

		public async Task<BiketimerProfile> GetUserProfile(string biketimerUserAccessToken)
		{
			var profile = await GetData<BiketimerProfile>(_getProfileAbsoluteUrl, biketimerUserAccessToken);
			return profile;
		}

		public async Task<IEnumerable<Spot>> GetSpots(string biketimerUserAccessToken)
		{
			var spots = await GetData<IEnumerable<Spot>>(_getSpotsAbsoluteUrl, biketimerUserAccessToken);
			return spots;
		}

		private async Task<T> GetData<T>(string resourceUrl, string biketimerUserAccessToken)
		{
			using (var client = new HttpClient())
			{
				var request = new HttpRequestMessage()
				{
					RequestUri = new Uri(_biketimerApiDomainUrl + resourceUrl),
					Method = HttpMethod.Get
				};

				request.Headers.Add("Authorization", "JWT " + biketimerUserAccessToken);

				var result = await client.SendAsync(request);
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

