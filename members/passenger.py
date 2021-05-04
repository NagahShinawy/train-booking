"""
created by Nagaj at 04/05/2021
"""
import datetime
import json
import os

from members import member as memb
from trip import Trip

activity_path = os.path.join("data", "activity.json")


class Passenger(memb.Member):
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
        with open(activity_path, "w") as f:
            json.dump(self.data[::-1], f, indent=4)

    @staticmethod
    def get_activities():
        data = []
        if not os.path.isfile(activity_path):
            return data
        with open(activity_path, "r") as f:
            data = json.load(f)
        return data
