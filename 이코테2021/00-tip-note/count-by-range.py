from bisect import bisect_left, bisect_right


def count_by_range(arr: list[int], lo: int, hi: int) -> int:
    """
        :param arr: a list sorted in ascending order
        :param lo: inclusive
        :param hi: inclusive
        
        :return: returns the number of items from lo(inclusive) to hi(inclusive)
    """
    return bisect_right(arr, hi) - bisect_left(arr, lo)