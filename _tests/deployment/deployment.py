
class Deployment:

    def __init__(self, apiEndpoint, identityEndpoint, cqlshCommand):
        self.ApiEndpoint = apiEndpoint
        self.IdentityEndpoint = identityEndpoint
        self.CqlshCommand = cqlshCommand