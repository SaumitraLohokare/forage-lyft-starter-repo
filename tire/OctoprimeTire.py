from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear):
        super().__init__(wear)

    def needs_service(self):
        return sum(self.wear) >= 3