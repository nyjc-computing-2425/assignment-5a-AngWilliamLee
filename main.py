seconds = input("Enter the number of seconds: ")

if not all(char in '0123456789' for char in str(seconds)):
  print("error1")
else:
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
  
      # if not all(char in '0123456789' for char in str(seconds)):
      #   print("error1")
      # else:
      seconds = int(seconds)
      hours = seconds // 3600
      minutes = (seconds % 3600) // 60
      remaining_seconds = seconds % 60
      hms = [hours, minutes, remaining_seconds]
      return hms

print(to_hms(seconds))
  
 



  
  




