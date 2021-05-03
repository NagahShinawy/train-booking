"""
created by Nagaj at 03/05/2021
"""
import uuid


class Trip:
    trips = []

    def __init__(self, pickup, dropoff, pickuptime, dropoff_time, train):
        self.trip_id = uuid.uuid4()
        self.pickup = pickup
        self.dropoff = dropoff
        self.pickuptime = pickuptime
        self.dropoff_time = dropoff_time
        self.train = train
        Trip.trips.append(self)

    def __repr__(self):
        return f"Trip<{self.trip_id}>"

    def show_trip_details(self):
        print(f"Trip ID : {self.trip_id}")
        print(f"Pickup  : {self.pickup}")
        print(f"DropOff : {self.dropoff}")
        print(f"From '{self.pickuptime}' To '{self.dropoff_time}'")
