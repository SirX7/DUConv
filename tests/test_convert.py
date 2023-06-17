import unittest
import pytest
from dataconverter import convert

# class Testconverter(unittest.TestCase): # Uncomment for unittest module

def test_to_kb():# Add self if using unittest module.
    #From MB to KB
    kb= convert.to_kb(5,"m")
    assert kb == "5,000.00 KB", "1 MB = 1,000 KB - resoult should be 5,000.00 KB (5*1,000=5,000.00)"

    # Form GB to KB
    kb= convert.to_kb(5,"G")
    assert kb == "5,000,000.00 KB", "1 GB = 1,000,000 KB(1,000^2) - resoult should be 5,000,000.00 KB (5*(1,000^2)=5,000,000.00)"

    # Form TB to KB
    kb= convert.to_kb(5,"t")
    assert kb == "5,000,000,000.00 KB", "1 TB = 1,000,000,000 KB(1000^3) - resoult should be 5,000,000,000.00 KB (5*(1,000^3)=5,000,000,000.00)"


def test_to_mb():# Add self if using unittest module.
    # From KB to MB
    mb= convert.to_mb(2_500,"K")
    assert mb == "2.50 MB", "1,000 KB = 1 MB - resoult should be 2.50 MB (2,500/1,000=2.50)"

    # From GB to MB
    mb= convert.to_mb(2.5,"g")
    assert mb == "2,500.00 MB", "1 GB = 1,000 MB - resoult should be 2,500.00 MB (2.5*1,000=2,500)"

    # From TB to MB
    mb= convert.to_mb(1.92,"t")
    assert mb == "1,920,000.00 MB", "1 TB = 1,000,000 MB (1,000^2) - resoult should be 1,920,000.00 MB (1.92*(1,000^2)=1,920,000.00)"


def test_to_gb():# Add self if using unittest module.
    # From KB to GB
    gb= convert.to_gb(9_207_000,"k")
    assert gb == "9.21 GB", "1 GB = 1,000,000 KB - resoult should be 9.20 GB (9,207,000/1,000,000=9.20)"

    # From MB to GB
    gb= convert.to_gb(6_270,"M")
    assert gb == "6.27 GB", "1 GB = 1,000 MB - resoult should be 6.27 GB (6,270/1,000=6.27)"

    # From TB to GB
    gb= convert.to_gb(0.23,"t")
    assert gb == "230.00 GB", "1 TB = 1,000 GB - resoult should be 230.00 GB (0.23*1,000=230)"


def test_to_tb():# Add self if using unittest module.
    # From KB to TB
    tb= convert.to_tb(7_981_905_000,"K")
    assert tb == "7.98 TB", "1 TB =  1,000,000,000 KB (1,000^3) - resoult should be 7.98 TB (7,981,905,000/(1,000^3)=7.98)"

    # From MB to TB
    tb= convert.to_tb(5_971_000,"m")
    assert tb == "5.97 TB", "1 TB =  1,000,000 MB (1,000^2) - resoult should be 5.97 TB (5,971,000/(1,000^2)=5.97)"

    # From GB to TB
    tb= convert.to_tb(9_100,"g")
    assert tb == "9.10 TB", "1 TB =  1,000 GB - resoult should be 9.10 TB (9,100/1,000=9.10)"




# Use this line when using unittest and want to exce from the script it self.
# if __name__ == "__main__":
#     unittest.main()