
class Indicators :

    def __init__(self, rule_engine) :
        self.rule_engine = rule_engine
        self.required_indicators = self.get_required_indicators()
    
    def get_required_indicators(self) :
        return {}  # key name : val indicator object from modules
    
    def update(self) :

        for indicator in self.required_indicators :
            self.required_indicators[indicator].run()