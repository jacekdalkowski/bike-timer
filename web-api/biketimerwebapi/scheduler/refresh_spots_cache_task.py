
class RefreshSpotsCacheTask:
	def __init__(self, spots_cache): 
		self.spots_cache = spots_cache
		pass

	def run(self):
		self.spots_cache.refresh()
