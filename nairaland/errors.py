class NairalandErrors(Exception):
    def __init__(self, message=None, http_status=None):
        super(NairalandErrors, self).__init__(message)

        self.message = message
        self.http_status = http_status


class AuthKeyError(NairalandErrors):
    """
    Auth Key Not Provided
    """
    pass

