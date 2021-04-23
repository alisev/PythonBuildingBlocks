class ExceptionTemplate(Exception):
  def __init__(self, exc_message: str, received_value):
    tmp_message = "Received value: {}.".format(str(received_value))
    error_message = '{} {}'.format(exc_message, tmp_message)
    super().__init__(error_message)
    
class AcceptedValuesException(ExceptionTemplate):
  message = "Variable '{}' values can only be '{}'."
  def __init__(self, variable_name: str, expected_values: list, received_value):
    error_message = self.message.format(variable_name, list_to_str(expected_values, "', '"))
    super().__init__(error_message, received_value)
    
class EqOrGreaterException(ExceptionTemplate):
  message = "Variable '{}' must be equal to {} or greater."
  def __init__(self, variable_name: str, expected_value, received_value):
    error_message = self.message.format(variable_name, str(expected_value))
    super().__init__(error_message, received_value)
