using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace Biketimer.Views.Stats
{
	public partial class UserStatsPage : ContentPage
	{
		public ListView ListView { get { return listView; } }

		public Button FilterByDateButton { get { return filterByDateButton; } }
		public Button FilterBySpotButton { get { return filterBySpotButton; } }
		public Button FilterBySegmentButton { get { return filterBySegmentButton; } }
		public Button SortButton { get { return sortButton; } }

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

			FilterByDateButton.Clicked += OnFilterByDateClicked;
			FilterBySpotButton.Clicked += OnFilterBySpotClicked;
			FilterBySegmentButton.Clicked += OnFilterBySegmentClicked;
			SortButton.Clicked += OnSortClicked;

			ListView.ItemsSource = new RunItem[]
			{
				new RunItem { Title = "AAA" },
				new RunItem { Title = "BBB" },
				new RunItem { Title = "CCC" }
			};
		}

		async void OnFilterByDateClicked(object sender, EventArgs e)
		{
			string[] spots = new string[] { "Today", "Last 2 days", "Last week" };
			string selectedSpot = await DisplayActionSheet("Period", "Cancel", null, spots);
		}

		async void OnFilterBySpotClicked(object sender, EventArgs e)
		{
			string[] spots = new string[] { "Kouty", "Spicak", "Kouty", "Spicak", "Kouty", "Spicak", "Kouty", "Spicak", "Kouty", "Spicak", "Kouty", "Spicak", "Kouty", "Spicak", "Kouty", "Spicak", "Kouty", "Spicak" };
			string selectedSpot = await DisplayActionSheet("Spot", "Cancel", null, spots);
		}

		async void OnFilterBySegmentClicked(object sender, EventArgs e)
		{
			string[] segments = new string[] { "Meadow", "Forest" };
			string selectedSegment = await DisplayActionSheet("Segment", "Cancel", null, segments);
		}

		async void OnSortClicked(object sender, EventArgs e)
		{
			string[] segments = new string[] { "Time", "Date - current first", "Date - oldest first" };
			var action = await DisplayActionSheet("Sort by", "Cancel", null, segments);
		}

		public class RunItem
		{
			public string Title { get; set; }
		}
	}
}

