import unittest
from datetime import datetime

import car_factory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_calliope(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_calliope(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wear = [0.1, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_calliope(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear = [0.1, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_calliope(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_glissade(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_glissade(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_glissade(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear = [0.9, 0.9, 0.9, 0.4]

        car = car_factory.CarFactory.create_glissade(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_palindrome(datetime.today(), last_service_date, warning_light_is_on, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        wear = [0.8, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_palindrome(datetime.today(), last_service_date, warning_light_is_on, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_palindrome(datetime.today(), last_service_date, warning_light_is_on, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        wear = [0.1, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_palindrome(datetime.today(), last_service_date, warning_light_is_on, wear)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_rorschach(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_rorschach(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_rorschach(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_rorschach(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_thovex(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wear = [0.8, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_thovex(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wear = [0.9, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_thovex(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wear = [0.2, 0.1, 0.1, 0.1]

        car = car_factory.CarFactory.create_thovex(datetime.today(), last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
