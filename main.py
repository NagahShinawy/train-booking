from member import Passenger, Admin, Driver
from train import Train
from trip import Trip


if __name__ == "__main__":
    admin = Admin("admin", "admin@gmail.com")
    passng = Passenger("john", "john@gmail.com", "2020-09-17")
    dr = Driver("driver1", "admin@gmail.com", 1)
    # admin.show_info()
    # print(admin.show_number_of_members)
    #
    # print("#" * 100)
    # admin.show_members()
    #
    # print("#" * 100)
    #
    # admin.show_drivers()
    # admin.show_passengers()
    #
    # print("#" * 100)
    # admin.show_member_trips(dr)
    # admin.show_member_trips(passng)
    train3456 = Train("3456", 200)
    print(train3456)
    trip = Trip("x", "y", "2020-09-21 10:00", "2020-09-21 12:00", train3456)
    print(trip)
    print("#" * 100)
    admin.assign_driver_to_trip(dr, trip)
    print(dr.trips)
    print(passng.trips)
    admin.show_member_trips(dr)
    admin.show_member_trips(passng)
