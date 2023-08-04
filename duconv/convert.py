"""This module helps convert to varios data unit"""


def to_kb(d: int | float, un:str)-> float:
    """Convert from MB, GB or TB to KB. 
    d:  data to convert, can be of type int or float.
    un: unit name, of type string"""

    kb = 0
    unit = "KB"
    unitNames = ["M", "G", "T"]
    
    un = un.upper()

    if un in unitNames:
        if un == "M":
            kb = d * 1_000
            return f"{kb:,.2f} {unit}"

        elif un == "G":
            kb = d * 1_000_000
            return f"{kb:,.2f} {unit}"

        elif un == "T":
            kb = d * 1_000_000_000
            return f"{kb:,.2f} {unit}"
    
    else:
        print(f"{un} is not a valid data unit name. Please try again by entering any of {unitNames}")
        return 0




def to_mb(d: int | float, un:str)-> float:
    """Convert from KB, GB, or TB to MB 
    d:  data to convert, can be of type int or float.
    un: unit name, of type string"""

    mb = 0
    unit = "MB"
    unitNames = ["K", "G", "T"]

    un = un.upper()

    if un in unitNames:
        if un == "K":
            mb = d / 1_000
            return f"{mb:,.2f} {unit}"

        elif un == "G":
            mb = d * 1_000
            return f"{mb:,.2f} {unit}"

        elif un == "T":
            mb = d * 1_000_000
            return f"{mb:,.2f} {unit}"
    
    else:
        print(f"{un} is not a valid data unit name. Please try again by entering any of {unitNames}")
        return 0


def to_gb(d: int | float, un:str)-> float:
    """Convert from KB, MB, or TB to GB 
    d:  data to convert, can be of type int or float.
    un: unit name, of type string"""

    gb = 0
    unit = "GB"
    unitNames = ["K", "M", "T"]

    un = un.upper()

    if un in unitNames:
        if un == "K":
            gb = d / 1_000_000
            return f"{gb:,.2f} {unit}"

        elif un == "M":
            gb = d / 1_000
            return f"{gb:,.2f} {unit}"

        elif un == "T":
            gb = d * 1_000
            return f"{gb:,.2f} {unit}"

    else:
        print(f"{un} is not a valid data unit name. Please try again by entering any of {unitNames}")
        return 0


def to_tb(d: int | float, un:str)-> float:
    """Convert from KB, MB. or GB to TB 
    d:  data to convert, can be of type int or float.
    un: unit name, of type string"""

    tb = 0
    unit = "TB"
    unitNames = ["K", "M", "G"]

    un = un.upper()

    if un in unitNames:
        if un == "K":
            tb = d / 1_000_000_000
            return f"{tb:,.2f} {unit}"

        elif un == "M":
            tb = d / 1_000_000
            return f"{tb:,.2f} {unit}"

        elif un == "G":
            tb = d / 1_000
            return f"{tb:,.2f} {unit}"

    else:
        print(f"{un} is not a valid data unit name. Please try again by entering any of {unitNames}")
        return 0