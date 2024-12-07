def mean_absolute_error(actual, calculated):
  """
  Calculates the Mean Absolute Error (MAE) between two lists.

  Args:
    actual: A list of actual values.
    calculated: A list of calculated values.

  Returns:
    The Mean Absolute Error.
  """
  if len(actual) != len(calculated):
    raise ValueError("Actual and calculated lists must have the same length.")

  errors = [abs(a - c) for a, c in zip(actual, calculated)]
  return sum(errors) / len(actual)

# Example usage:
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]

mae = mean_absolute_error(actual, calculated)
print(f"Mean Absolute Error: {mae}")