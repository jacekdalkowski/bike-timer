from injector import Module
from scheduler import Scheduler
from injector import Injector, inject, Key
from refresh_spots_cache_task import RefreshSpotsCacheTask
from ..cache.cache_definitions import SpotsCacheKey

SchedulerKey = Key('SchedulerKey')

class SchedulerModule(Module):

    def configure(self, binder):
    	spots_cache = binder.injector.get(SpotsCacheKey)
    	refresh_spots_cache_task = RefreshSpotsCacheTask(spots_cache)
        scheduler_instance = Scheduler(refresh_spots_cache_task)
        binder.bind(SchedulerKey, to=scheduler_instance)
