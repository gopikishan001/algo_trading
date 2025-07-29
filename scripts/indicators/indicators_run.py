
class Indicators :

    def __init__(self) :
        self.required_indicators = self.get_required_indicators()
    
    def get_required_indicators(self) :
        return {}  # key name : val indicator object from modules
    
    def update(self) :

        for indicator in self.required_indicators :
            self.required_indicators[indicator].run()