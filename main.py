def to_hms(seconds: int) -> list:
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated

    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    """

    if type(seconds) == int and seconds >= 0:
      hours = seconds // 3600
      seconds %= 3600
      minutes = seconds // 60
      seconds %= 60
      return [hours, minutes, seconds]
    else:
      print("Unsupported input type.")


# user_input = input("Enter the number of seconds: ")
# print(to_hms(user_input))

  
  




