"""
created by Nagaj at 03/05/2021
"""
from errors.exceptions import NoPermission
from members import admin


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
        if isinstance(self, admin.Admin):
            return admin.Admin._number_of_members
        raise NoPermission(NoPermission.message.format(self))
