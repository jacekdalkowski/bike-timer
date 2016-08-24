using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Stats
{
	public partial class UserStatsPage : ContentPage
	{
		public ListView ListView { get { return listView; } }

		public UserStatsPage()
		{
			Title = "Me";

			InitializeComponent();

			//AbsoluteLayout simpleLayout = new AbsoluteLayout
			//{
			//	BackgroundColor = Color.Blue.WithLuminosity(0.9),
			//	VerticalOptions = LayoutOptions.FillAndExpand
			//};

			//Label topLeftLabel = new Label
			//{
			//	Text = "Top Left",
			//	TextColor = Color.Black
			//};

			//AbsoluteLayout.SetLayoutBounds(topLeftLabel,
			//	new Rectangle(0f,
			//		0f, AbsoluteLayout.AutoSize, AbsoluteLayout.AutoSize));

			//simpleLayout.Children.Add(topLeftLabel);

			//this.Content = new StackLayout
			//{
			//	Children = {
			//		header,
			//		simpleLayout
			//	}
			//};

			ListView.ItemsSource = new RunItem[]
			{
				new RunItem { Title = "AAA" },
				new RunItem { Title = "BBB" },
				new RunItem { Title = "CCC" }
			};
		}

		public class RunItem
		{
			public string Title { get; set; }
		}
	}
}

