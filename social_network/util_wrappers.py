class InputWrapper:
    """
    Wrapper for input function
    """
    def read_input(self, str_input: str) -> None:
        return input(str_input)


class PrintWrapper:
    """
    Wrapper for print function
    """
    def output(self, str_input: str) -> None:
        print(str_input)
