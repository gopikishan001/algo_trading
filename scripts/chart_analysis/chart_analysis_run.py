
class Chart_analysis :

    def __init__(self, rule_engine) :
        self.rule_engine = rule_engine
        self.required_analysis = self.get_required_analysis()
    
    def get_required_analysis(self) :
        return {}  # key name : val candel object from modules
    
    def update(self) :

        for module in self.required_analysis :
            self.required_analysis[module].run()