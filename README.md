# Mean Absolute Error (MAE) Calculation

This Python function calculates the Mean Absolute Error (MAE) between two lists of values.

def mean_absolute_error(actual, calculated):
  """
  Calculates the Mean Absolute Error (MAE) between two lists.

  Args:
    actual: A list of actual values.
    calculated: A list of calculated values.

  Returns:
    The Mean Absolute Error.

  Raises:
    ValueError: If the lengths of the input lists are not equal.
  """
  if len(actual) != len(calculated):
    raise ValueError("Actual and calculated lists must have the same length.")

  errors = [abs(a - c) for a, c in zip(actual, calculated)]
  return sum(errors) / len(actual)
