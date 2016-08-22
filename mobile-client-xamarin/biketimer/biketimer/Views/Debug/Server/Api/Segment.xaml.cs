using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Server.Api
{
	public partial class Segment : ContentPage
	{
		private NavigationPage _topNavigationPage;

		public Segment(NavigationPage topNavigationPage, Biketimer.Segment segment)
		{
			_topNavigationPage = topNavigationPage;

			InitializeComponent();
		}
	}
}

