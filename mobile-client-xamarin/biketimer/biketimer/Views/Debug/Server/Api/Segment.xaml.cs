using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Server.Api
{
	public partial class Segment : ContentPage
	{
		private NavigationPage _topNavigationPage;

		public Segment(NavigationPage topNavigationPage, Biketimer.BiketimerApiServer.Entities.Segment segment)
		{
			_topNavigationPage = topNavigationPage;

			var segmentViewModel = new SegmentViewModel(segment);
			BindingContext = segmentViewModel;

			InitializeComponent();
		}
	}
}

