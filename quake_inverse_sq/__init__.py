"""
Inverse square root implementations. (Implementation from Wikipedia and math.h)
"""
import logging
logger = logging.getLogger('quake_inverse_sq')
try:
    from ._sqrt import coarse_inv_sqrt as __c
    from ._sqrt import fined_inv_sqrt as __f
except ImportError:
    logger.warning('No native extension found. Falling back to pure python implementation.')
    from ctypes import c_float, c_int32, cast, byref, POINTER
    from math import sqrt
    def __c(number: float):
        THREEHALFS = 1.5
        x2 = number * 0.5
        y = c_float(number)
        WHAT_THE_FUCK = 0x5f3759df

        i = cast(byref(y), POINTER(c_int32)).contents.value
        i = c_int32(WHAT_THE_FUCK - (i >> 1))
        y = cast(byref(i), POINTER(c_float)).contents.value

        y = y * (THREEHALFS - (x2 * y * y))
        return y
    def __f(number: float):
        return 1/sqrt(x)

def coarse_inv_sqrt(number:float) -> float:
    """
    Coarse inverse square root. (Implementation from [Wikipedia](https://en.wikipedia.org/wiki/Fast_coarse_inv_sqrt))
    """
    if number <= 0:
        raise ZeroDivisionError
    elif not isinstance(number, (float,int)):
        raise ValueError("Inappropriate argument value")
    return __c(number)

def fined_inv_sqrt(number: float) -> float:
    """
    Fined inverse square root. (Implementation from math.h)
    """
    if number <= 0:
        raise ZeroDivisionError
    elif not isinstance(number, (float,int)):
        raise ValueError("Inappropriate argument value")
    return __f(number)

