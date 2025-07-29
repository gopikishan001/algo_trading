
class Candels :

    def __init__(self) :
        self.required_candels = self.get_required_candels()
    
    def get_required_candels(self) :
        return {}  # key name : val candel object from modules
    
    def update(self) :

        for candel in self.required_candels :
            self.required_candels[candel].run()