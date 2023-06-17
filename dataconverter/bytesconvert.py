"""A Module that helps Convert Bytes to KB, MB, GB, or TB."""

def bytes_converter(b: int|float) -> float:
    """Converts bytes into KB, MB, GB, or TB"""

    unitSize = 1_000
    unitNames = ["bytes", "KB", "MB", "GB", "TB"]

    for un in unitNames:
        if b < unitSize:
            return f"{b:.3f} {un}"
        b /= unitSize
        
def data_to_bytes(d:int|float, un: str)-> float:
    """Converts from any of KB, MB, GB, or TB to bytes"""
    unitNames= ["K","M","G","T"]
    b = 0

    unit = un.upper()

    if unit in unitNames:
        if unit == "K":
            b = d*1_000
            return f"{b:.3f} bytes"

        elif unit == "M":
            b = d*1_000_000
            return f"{b:.3f} bytes"

        elif unit == "G":
            b = d*1_000_000_000
            return f"{b:.3f} bytes"

        elif unit == "T":
            b = d*1_000_000_000_000
            return f"{b:.3f} bytes"
    else:
        print(f"{un} is not a valid data unit name. Please try again by entering any of {unitNames}")