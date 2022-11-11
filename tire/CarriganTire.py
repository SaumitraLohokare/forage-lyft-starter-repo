from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear):
        super().__init__(wear)

    def needs_service(self):
        for tire_wear in self.wear:
            if tire_wear >= 0.9:
                return True
        return False