from injector import Module
from ..cache_definitions import SpotsCacheKey
from spots_cache import SpotsCache
from ...db.repositories.repositories_definitions import SpotsRepository

class MemoryCacheModule(Module):

    def configure(self, binder):
        spots_repository = binder.injector.get(SpotsRepository)
        spots_cache_instance = SpotsCache(spots_repository) 
        binder.bind(SpotsCacheKey, to=spots_cache_instance)
