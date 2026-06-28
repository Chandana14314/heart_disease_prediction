import sys

class CustomException(Exception):

    def __init__(self, error_message, error_detail=sys):
        self.error_message = CustomException.get_error_message(
            error_message,
            error_detail
        )

    @staticmethod
    def get_error_message(error_message, error_detail):
        _, _, exc_tb = error_detail.exc_info()

        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno

            return f"Error occurred in {file_name} at line {line_number}: {error_message}"

        return str(error_message)

    def __str__(self):
        return self.error_message