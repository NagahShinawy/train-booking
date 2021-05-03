"""
created by Nagaj at 03/05/2021
"""


class Train:
    def __init__(self, number, seats):
        self.number = number
        self.seats = seats

    def __repr__(self):
        return f"Train#{self.number}"

    def show_train_details(self):
        print(f"Number: {self.number}")
        print(f"Seats: {self.seats}")
