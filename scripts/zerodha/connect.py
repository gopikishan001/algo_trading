from kiteconnect import KiteConnect

class ZerodhaConnector:
    def __init__(self, api_key, api_secret, request_token):
        self.api_key = api_key
        self.api_secret = api_secret
        self.request_token = request_token
        self.kite = None

    def connect(self):
        kite = KiteConnect(api_key=self.api_key)
        data = kite.generate_session(self.request_token, api_secret=self.api_secret)
        kite.set_access_token(data["access_token"])
        self.kite = kite
        return kite