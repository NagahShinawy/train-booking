"""
created by Nagaj at 03/05/2021
"""
import datetime
import json
import os
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
        self.data = self.get_activities()

    def show_info(self):
        super().show_info()
        print(f"Join Date: {self.created}")

    @staticmethod
    def list_trips():
        for trip in Trip.available:
            print(trip)

    def book_trip(self, trip: Trip):
        action = "Book"
        if trip.train.seats == 0:
            print("No Seats You Can Not Book")
        elif trip in self.trips:
            print(f"Already Booked")
        else:
            trip.train.seats -= 1
            trip.show_trip_details()
            self.trips.append(trip)
            print(f"Your {trip} Was Booked!")
        self.__save_activity(trip, action)

    def cancel_trip(self, trip):
        action = "Cancel"
        if trip in self.trips:
            self.trips.remove(trip)
            print(f"{trip} for {self} was Canceled")
            trip.train.seats += 1
        else:
            print(f"{trip} was not booked")
        self.__save_activity(trip, action)

    def __save_activity(self, trip, action):
        activity = {
            "user": {"username": self.username, "email": self.email},
            "trip": {
                "trip_id": repr(trip),
                "pickup": trip.pickup,
                "dropoff": trip.dropoff,
                "pickuptime": trip.pickuptime,
                "dropoff_time": trip.dropoff_time,
                "train": trip.train.number,
            },
            "action": action,
            "datetime": datetime.datetime.strftime(
                datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"
            ),
        }
        self.data.append(activity)
        with open("activity.json", "w") as f:
            json.dump(self.data[::-1], f, indent=4)

    @staticmethod
    def get_activities():
        data = []
        if not os.path.isfile("activity.json"):
            return data
        with open("activity.json", "r") as f:
            data = json.load(f)
        return data


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
    def assign_trip_to_driver(driver: Driver, trip):
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
