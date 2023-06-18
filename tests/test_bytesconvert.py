import unittest
import pytest
from dataconverter import bytesconvert

def test_bytes_converter() -> None:
    assert bytesconvert.bytes_converter(5_482) == '5.482 KB'

    assert bytesconvert.bytes_converter(5_482_000) == '5.482 MB'

    assert bytesconvert.bytes_converter(5_482_100_000) == '5.482 GB'

    assert bytesconvert.bytes_converter(5_482_200_500_000) == '5.482 TB'

def test_data_to_bytes() -> None:
    assert bytesconvert.data_to_bytes(5.482,"k") == "5,482.000 bytes"

    assert bytesconvert.data_to_bytes(5.482,"M") == "5,482,000.000 bytes"

    assert bytesconvert.data_to_bytes(5.482,"g") == "5,482,000,000.000 bytes"

    assert bytesconvert.data_to_bytes(5.482,"t") == "5,482,000,000,000.000 bytes"

    assert bytesconvert.data_to_bytes(5.482,"b") == 0

