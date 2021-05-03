"""
created by Nagaj at 03/05/2021
"""
from exceptions import NoPermission
from trip import Trip


class Member:
    _number_of_members = 0
    members = []

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.trips = []
        Member._number_of_members += 1
        Member.members.append(self)

    def __repr__(self):
        return f"<{self.__class__.__name__}><{self.username}>"

    def __contains__(self, item):
        return item in self.trips

    def __getitem__(self, item):
        return self.trips[item]

    def show_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    @property
    def show_number_of_members(self):
        if isinstance(self, Admin):
            return Admin._number_of_members
        raise NoPermission(NoPermission.message.format(self))


class Passenger(Member):
    def __init__(self, username, email, created):
        super().__init__(username, email)
        self.created = created

    def show_info(self):
        super().show_info()
        print(f"Join Date: {self.created}")

    def list_trips(self):
        for trip in Trip.trips:
            print(trip)

    def book_trip(self, trip):
        pass

    def cancel_trip(self, trip):
        pass

    def list_trip_history(self):
        pass


class Driver(Member):
    def __init__(self, username, email, driver_license):
        super().__init__(username, email)
        self.driver_license = driver_license

    def show_info(self):
        super().show_info()
        print(f"License {self.driver_license}")


class Admin(Member):
    # todo : add decorators to show members

    PERMISSION = "all"

    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def assign_driver_to_trip(driver: Driver, trip):
        driver.trips.append(trip)

    def show_members(self):
        for member in self.members:
            print(member)

    def show_drivers(self):
        for member in self.members:
            if isinstance(member, Driver):
                print(member)

    def show_passengers(self):
        for member in self.members:
            if isinstance(member, Passenger):
                print(member)

    @staticmethod
    def show_member_trips(member):
        for trip in member.trips:
            print(trip)
