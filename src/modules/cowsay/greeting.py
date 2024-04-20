import cowsay
from typing import LiteralString


def say_message(message: str, intensity: int) -> LiteralString:
    """_summary_

    Args:
        your_name (str): _description_
    """
    return cowsay.get_output_string("cow", f"{message}{intensity * '!'}")
