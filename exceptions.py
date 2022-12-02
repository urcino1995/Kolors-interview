
class CantSellThisDay(Exception):
    """Raised when the Sale day is less that Shopping day"""
    ...


class DayDoesNotExist(Exception):
    """Raised when the day entered is greater than array's days"""
    ...


class LengthNotAllowed(Exception):
    """Raised when the length array is greater than allowed"""
    ...


class LengthElementNotAllowed(Exception):
    """Raised when the length of element is greater than allowed"""
    ...
