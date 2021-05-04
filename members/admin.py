"""
created by Nagaj at 04/05/2021
"""
from members import member as memb
from members import passenger
from members import driver as drv


class Admin(memb.Member):
    # todo : add decorators to show members

    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def assign_trip_to_driver(driver: drv.Driver, trip):
        driver.trips.append(trip)

    def show_members(self):
        for member in self.members:
            print(member)

    def show_drivers(self):
        for member in self.members:
            if isinstance(member, drv.Driver):
                print(member)

    def show_passengers(self):
        for member in self.members:
            if isinstance(member, passenger.Passenger):
                print(member)

    @staticmethod
    def show_member_trips(member):
        for trip in member.trips:
            print(trip)
