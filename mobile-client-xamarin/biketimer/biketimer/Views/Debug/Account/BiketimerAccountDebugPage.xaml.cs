using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer
{
	public partial class BiketimerAccountDebugPage : ContentPage
	{
		
		public BiketimerAccountDebugPage(BiketimerAccountDebugPageViewModel viewModel)
		{
			InitializeComponent();
			BindingContext = viewModel;
		}
	}
}

