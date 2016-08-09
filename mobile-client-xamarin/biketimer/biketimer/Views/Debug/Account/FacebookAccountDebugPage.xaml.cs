using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Debug.Account
{
	public partial class FacebookAccountDebugPage : ContentPage
	{
		
		public FacebookAccountDebugPage(FacebookAccountDebugPageViewModel viewModel)
		{
			InitializeComponent();
			BindingContext = viewModel;
		}
	}
}

