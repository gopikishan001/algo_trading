
import os
from scripts.zerodha.connect import ZerodhaConnector
from datetime import time
from scripts.utils.rule_engine import Rule_engine

class TradingApp:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.request_token = os.getenv("REQUEST_TOKEN")
        self.kite = None
        self.connected = False

    def connect_to_broker(self):
        if not all([self.api_key, self.api_secret, self.request_token]):
            print("Missing environment variables.")
            return 
        
        connector = ZerodhaConnector(self.api_key, self.api_secret, self.request_token)
        self.kite = connector.connect()
        profile = self.kite.profile()
        print(f"*** Connected to: {profile['user_name']}\n\n")
        self.connected = True


    def run(self):
        self.rule_engine = Rule_engine(self.kite)
        
        while self.rule_engine.is_market_open() :
            self.rule_engine.run()
            time.sleep(1) 

                
if __name__ == "__main__":
    app = TradingApp()
    app.connect_to_broker()

    if app.connected :
        app.run()
        app.kite.logout()
