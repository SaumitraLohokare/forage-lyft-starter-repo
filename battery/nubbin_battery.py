from battery import Battery
from datetime import datetime

class NubbinBattery(Battery):
    def __init__(self, current_date: datetime, last_service_date: datetime):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < self.current_date