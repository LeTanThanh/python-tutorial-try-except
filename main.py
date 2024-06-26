if __name__ == "__main__":
  # Handling exceptions

  """
  try:
    # code that may cause error
  except:
    # handle error
  """

  # try:
  #   print("Enter the net sales for")

  #   previous = float(input("- Previous period:"))
  #   current = float(input("- Current period:"))

  #   change = (current - previous) * 100 / previous

  #   if change > 0:
  #     result = f"Sales increase {abs(change)}%"
  #   else:
  #     result = f"Sales decrease {abs(change)}%"

  #   print(result)
  # except:
  #   print("Error! Please enter a number for net sales")

  # Catching specific exceptions

  # try:
  #   print("Enter the net sales for")

  #   previous = float(input("- Previous period:"))
  #   current = float(input("- Current period:"))

  #   change = (current - previous) * 100 / previous

  #   if change > 0:
  #     result = f"Sales increase {abs(change)}%"
  #   else:
  #     result = f"Sales decrease {abs(change)}%"

  #   print(result)
  # except ValueError:
  #   print("Error! Please enter a number for net sales")

  # Handling multiple exceptions

  try:
    print("Enter the net sales for")

    previous = float(input("- Previous period:"))
    current = float(input("- Current period:"))

    change = (current - previous) * 100 / previous

    if change > 0:
      result = f"Sales increase {abs(change)}%"
    else:
      result = f"Sales decrease {abs(change)}%"

    print(result)
  except ValueError:
    print("Error! Please enter a number for net sales.")
  except ZeroDivisionError:
    print("Error! The prior net sales cannot be zero.")
  except Exception as error:
    print(error)
