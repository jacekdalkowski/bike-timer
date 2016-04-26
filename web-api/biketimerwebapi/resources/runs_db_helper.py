
logger = logging.getLogger('resources')

class RunsDbHelper(Resource):

	def __init__(self, runs_repository):
        self.runs_repository = runs_repository