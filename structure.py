from typing import List

from exceptions import LengthNotAllowed, LengthElementNotAllowed


class ListBasedOne:
    """
    This is a Custom Datatype.
    Is a list start in one instead zero
    """

    MINIMUM_LENGTH = 1
    MAXIMUM_LENGTH = 100000
    MINIMUM_LENGTH_EACH_ELEMENT = 0
    MAXIMUM_LENGTH_EACH_ELEMENT = 10000

    def __init__(self, prices: List):
        self.list = self.is_valid_prices(prices)

    def __getitem__(self, index):
        return self.list[index-1]

    def __getitems__(self):
        return self.list

    def __setitem__(self, index, value):
        self.list[index-1] = value

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        return self

    def is_valid_prices(self, prices: str) -> List:
        prices = self.conver_to_list(prices)
        if not self.MINIMUM_LENGTH <= len(prices) <= self.MAXIMUM_LENGTH:
            raise LengthNotAllowed("La cantidad de elementos que ingresaste en el array no está permitida.")
        return prices

    def conver_to_list(self, prices: str) -> List:
        if prices:
            prices = prices.split(',')
            prices = list(map(self.validate_each_element, prices))
            return prices
        return []

    def validate_each_element(self, price: str) -> int:
        if not self.MINIMUM_LENGTH_EACH_ELEMENT <= len(price) <= self.MAXIMUM_LENGTH_EACH_ELEMENT:
            raise LengthElementNotAllowed("El valor del elemento no puede ser menor de"
            f" {self.MINIMUM_LENGTH_EACH_ELEMENT} o mayor a {self.MAXIMUM_LENGTH_EACH_ELEMENT}")
        return int(price)
