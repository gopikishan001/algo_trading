
from scripts.kite.fetch_data import fetch_data

class Cache :

    def __init__(self) :
        self.data = {}
        self.counter = 0
        self.open_trades = {}
        self.completed_trades = {}
        self.required_symbols = self.get_required_symbols()

    def get_required_symbols(self) :
        return ["NSE:NIFTY 50"]
        # key name : val indicator object from modules
    
    
    def update(self, kite) :

        self.counter += 1

        for symbol in self.required_symbols :
            if symbol not in self.data : self.data[symbol] = {}
            self.data[symbol][self.counter] = fetch_data(kite, symbol)
