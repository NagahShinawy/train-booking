"""
created by Nagaj at 03/05/2021
"""


class NoPermission(Exception):
    message = "Member '{}' Has No Permission"
    code = 403
