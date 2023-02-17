# quake 3's fastest inverse square root

This module is a port from Quake 3's inverse square root algorithm.

## Installation

1. Get yourself a C compiler (like gcc, clang or msvc)
2. Run `python setup.py install`
3. Enjoy!

## Build

1. Get yourself a C compiler (like gcc, clang or msvc)
2. Run `python setup.py build bdist_wheel sdist`
3. Check the `dist` folder for the wheel and source distribution

## Documentation

`quake_inverse_sq.coarse_inv_sqrt(number: float) -> float`  
This is fastest inverse square root algorithm. It is not as accurate as the `quake_inverse_sq.fined_inv_sqrt` function, but it is much faster. It is implemented from this [wikipedia](https://en.wikipedia.org/wiki/Fast_coarse_inv_sqrt)  
  
`quake_inverse_sq.fined_inv_sqrt(number: float) -> float`
This is the original inverse square root algorithm. It is more accurate than the `quake_inverse_sq.coarse_inv_sqrt` function, but it is slower. It is implemented from `math.h`
