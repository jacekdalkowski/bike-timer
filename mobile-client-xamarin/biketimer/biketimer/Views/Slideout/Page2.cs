using System;

using Xamarin.Forms;

namespace biketimer
{
	public class Page2 : ContentPage
	{
		public Page2()
		{
			Content = new StackLayout
			{
				Children = {
					new Label { Text = "Hello ContentPage" }
				}
			};
		}
	}
}


