using System;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Biketimer.Views.Helpers
{
	public static class ActionSheet
	{
		public static async Task<Tuple<string, string>> DisplayKeyValueActionSheet(this Xamarin.Forms.Page page, string title, string cancel, 
		                                  string destruction, IEnumerable<Tuple<string, string>> buttons)
		{
			// TODO: make sure that labels and ids are distinct
			string[] buttonsLabels = buttons.Select(b => b.Item1).ToArray();
			string actionSheetResult = await page.DisplayActionSheet(title, cancel, destruction, buttonsLabels);
			if (string.Equals(cancel, actionSheetResult, StringComparison.Ordinal))
			{
				return null;
			}

			Tuple<string, string> keyValueResult = buttons.Single(b => string.Equals(b.Item1, actionSheetResult, StringComparison.Ordinal));
			return keyValueResult;
		}
	}
}

