from injector import Injector, inject, Key
CheckpointPassesToRunsComputerKey = Key('CheckpointPassesToRunsComputerKey')

from injector import Module
from .db.repositories.repositories_definitions import SpotsRepository
from .db.repositories.repositories_definitions import RunsRepository
from .cache.cache_definitions import SpotsCacheKey
from checkpoint_passes_to_runs_computer import CheckpointPassesToRunsComputer

class CheckpointPassesToRunsComputerModule(Module):

    def configure(self, binder):
        checkpoint_passes_repository = binder.injector.get(SpotsRepository)
        runs_repository = binder.injector.get(RunsRepository)
        spots_cache_instance = binder.injector.get(SpotsCacheKey)

        checkpoint_passes_to_runs_computer = CheckpointPassesToRunsComputer(spots_cache_instance, 
            checkpoint_passes_repository, runs_repository)

        binder.bind(CheckpointPassesToRunsComputerKey, to=checkpoint_passes_to_runs_computer)