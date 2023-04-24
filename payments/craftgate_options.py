CRAFTGATE_BASE_URL = 'https://sandbox-api.craftgate.io'
CRAFTGATE_API_KEY = 'sandbox-lRbJrriwrVELcbmYotAcyaZglWmRSBnh'
CRAFTGATE_SECRET_KEY = 'sandbox-EasuerenJrydAWtoldiRcbtSRQigBmVt'
CRAFTGATE_RANDOM_STRING = "191213010217"


class CraftgateOptions():
    def __init__(self, options=None):
        self.api_key = CRAFTGATE_API_KEY
        self.secret_key = CRAFTGATE_SECRET_KEY
        self.base_url = CRAFTGATE_BASE_URL
        self.random_string = CRAFTGATE_RANDOM_STRING
        self.language = None

        if options is not None:
            self.api_key = options.get('apiKey', CRAFTGATE_API_KEY)
            self.secret_key = options.get('secretKey', CRAFTGATE_SECRET_KEY)
            self.base_url = options.get('baseUrl', CRAFTGATE_BASE_URL)
            self.random_string = options.get('randomString', CRAFTGATE_RANDOM_STRING)
            self.language = options.get('language')

    def get_api_key(self):
        return self.api_key

    def get_secret_key(self):
        return self.secret_key

    def get_base_url(self):
        return self.base_url

    def get_random_string(self):
        return self.random_string

    def get_language(self):
        return self.language

    def to_dict(self):
        return {
            'api_key': self.api_key,
            'secret_key': self.secret_key,
            'base_url': self.base_url,
            'language': self.language,
        }
