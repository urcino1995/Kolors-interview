from typing import List

from exceptions import (CantSellThisDay,
                        DayDoesNotExist)


def validate_sale_day(shopping_day: int, sale_day: int, prices_length: int):
    """
    Validate sale day against shopping day and day of prices
    Sale day can't be same that shopping day
    Sale day can't be greater than prices length
    Args:
        Shopping day: number
        Sale day: number
        Prices length: number
    Return:
        None
    Raises:
        CantSellThisDay or CantSellThisDay
    """
    if sale_day <= shopping_day:
        raise CantSellThisDay("No puedes vender un día antes, el mismo día de compra")
    if sale_day > prices_length:
        raise DayDoesNotExist("El día de venta no puede ser mayor a los días de precios")


def validate_shopping_day(shopping_day: int, prices_length: int):
    """
    Validate sale day against shopping day and day of prices
    Sale day can't be same that shopping day
    Sale day can't be greater than prices length
    Args:
        Shopping day: number
        Sale day: number
        Prices length: number
    Return:
        None
    Raises:
        CantSellThisDay or CantSellThisDay
    """
    if shopping_day > prices_length:
        raise DayDoesNotExist("El día de compra no puede ser mayor a los días de precios")
