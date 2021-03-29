
class ServerConfig(object):
    # TODO: What am I trying to accomplish here? Should this just be in the other config helper?
    _instance = None
    _rate_limiter = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ServerConfig, cls).__new__(cls)

        return cls._instance

    def get_rate_limiter(self):
        return self._rate_limiter

    def set_rate_limiter(self, rate_limiter):
        self._rate_limiter = rate_limiter

