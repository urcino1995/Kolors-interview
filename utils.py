from typing import List


def calculate_financial_gain(prices: List[int], sale_day: int, shopping_day: int) -> int:
    """
    Args:
        prices: List of integers
    Return:
        Int : gain
    """
    gain  = prices[sale_day] - prices[shopping_day]
    if gain <= 0:
        gain = 0
    return f"Ganancias: {gain}"
