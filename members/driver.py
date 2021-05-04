"""
created by Nagaj at 04/05/2021
"""
from members import member as memb


class Driver(memb.Member):
    def __init__(self, username, email, driver_license):
        super().__init__(username, email)
        self.driver_license = driver_license

    def show_info(self):
        super().show_info()
        print(f"License {self.driver_license}")
