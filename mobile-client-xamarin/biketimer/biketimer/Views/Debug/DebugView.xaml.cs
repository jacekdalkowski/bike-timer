using System;
using System.Collections.Generic;
using Biketimer.Views.Debug.Account;
using Xamarin.Forms;

namespace Biketimer.Views.Debug
{
	public partial class DebugView : NavigationPage
	{
		public DebugView() : base()
		{
			InitializeComponent();
			DebugViewList debugViewList = new DebugViewList(this);
			PushAsync(debugViewList);
		}
	}
}

