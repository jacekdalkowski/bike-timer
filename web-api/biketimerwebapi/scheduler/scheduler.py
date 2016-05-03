import time
from threading import Timer

class Scheduler:

	def print_time(self):
		print "From print_time", time.time()

	def __init__(self, refresh_spots_cache_task):
		self.refresh_spots_cache_task = refresh_spots_cache_task
		Timer(5, self.print_time, ()).start()



