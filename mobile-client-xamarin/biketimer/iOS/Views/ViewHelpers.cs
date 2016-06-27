using System;
using UIKit;
using System.Linq;

namespace Biketimer.iOS
{
	public class ViewHelpers
	{
		public static UIView GetTopmostView(UIView view)
		{
			UIView currentView = view;
			while (currentView.Superview != null)
			{
				currentView = currentView.Superview;
			}
			return currentView;

		}

		public static LoadingOverlay AddLoadingOverlay(UIView view)
		{
			var bounds = UIScreen.MainScreen.Bounds;
			var loadingOverlay = new LoadingOverlay(bounds);
			UIView topmostView = GetTopmostView(view);
			topmostView.Add(loadingOverlay);
			return loadingOverlay;
		}

		public static void RemoveLoadingOverlay(UIView view)
		{
			UIView topmostView = GetTopmostView(view);
			topmostView.Subviews[0].Subviews.Where(v => v is LoadingOverlay)
					   .ToList()
			           .ForEach(v =>
							{
								v.RemoveFromSuperview();
								v.Dispose();
							});
		}
	}
}

