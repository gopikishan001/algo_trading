from scripts.utils.cache import Cache
from datetime import datetime, time
from scripts.zerodha.trade import Trade
from scripts.candels.candels_run import Candels
from scripts.indicators.indicators_run import Indicators
from scripts.chart_analysis.chart_analysis_run import Chart_analysis

class Rule_engine :
    def __init__(self, kite) :

        self.required_symbols = []
        self.kite = kite 
        self.cache = Cache(self) 
        self.trade = Trade(self)
        self.candels = Candels(self)
        self.indicators = Indicators(self)
        self.chart_analysis = Chart_analysis(self)

        self.update_pre_placed_trades()
    
    def run(self) :
        self.cache.update(self.required_symbols)

        if self.is_after_3pm() :
            self.stop_all_open_trade()

        else :
            self.check_for_new_trades()

    def stop_all_open_trade(self) :
        for open_trade_key in self.cache.open_trades :
            self.trade.sell_order()
            self.cache.open_trades[open_trade_key]

    def update_pre_placed_trades(self) :
        orders = self.trade.fetch_placed_orders()
        for order in orders :
            pass
            # self.cache.open_trades  update them >>

    def check_for_new_trades(self) :
        pass

    def is_market_open(self):
        now = datetime.now()
        is_weekday = 0 <= now.weekday() <= 4
        market_start = time(9, 30)
        market_end = time(15, 30)
        is_within_time = market_start <= now.time() <= market_end
        return is_weekday and is_within_time
    
    def is_after_3pm(self):
        now = datetime.now().time()
        return now > time(15, 0)