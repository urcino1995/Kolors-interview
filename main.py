from typing import List, Tuple

from structure import ListBasedOne
from utils import calculate_financial_gain
from validations import validate_sale_day, validate_shopping_day
from exceptions import (CantSellThisDay, DayDoesNotExist,
                        LengthNotAllowed, LengthElementNotAllowed)


def get_price() -> List[int]:
    try:
        print("Por favor ingrese el arreglo de precios, separando cada elemento por comas (,): ")
        prices = input()
        prices = ListBasedOne(prices)
        return prices
    except LengthNotAllowed as lna:
        print(lna)
        get_price()
    except LengthElementNotAllowed as lena:
        print(lena)
        get_price()


def get_days(prices_length: int) ->Tuple:
    try:
        print("Ingresa el día que quieres Comprar: ")
        shopping_day = int(input())
        validate_shopping_day(shopping_day, prices_length)
        print(f"Ingresa el día que quieres Vender (Día máximo {prices_length}): ")
        sale_day = int(input())
        validate_sale_day(shopping_day, sale_day, prices_length)
        return shopping_day, sale_day
    except CantSellThisDay as cstd:
        print(cstd)
        get_days(prices_length)
    except DayDoesNotExist as ddne:
        print(ddne)
        get_days(prices_length)


def main():
    prices = get_price()
    shopping_day, sale_day = get_days(len(prices))
    gain = calculate_financial_gain(prices, sale_day, shopping_day)
    print(gain)


if __name__ == '__main__':
    main()

