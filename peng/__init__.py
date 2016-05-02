# __init__.py
# Copyright (c) 2013-2016 Pablo Acosta-Serafini
# See LICENSE for details
# pylint: disable=C0111,W0622

# Intra-package imports
from .version import __version__
from .functions import (
    EngPower,
    NumComp,
    no_exp,
    peng,
    peng_float,
    peng_frac,
    peng_int,
    peng_mant,
    peng_power,
    peng_suffix,
    peng_suffix_math,
    pprint_vector,
    remove_extra_delims,
    round_mantissa,
    to_scientific_string,
    to_scientific_tuple
)
from .touchstone import read_touchstone, write_touchstone
from .wave_core import Point, Waveform
from .wave_functions import (
    acos,
    acosh,
    asin,
    asinh,
    atan,
    atanh,
    average,
    ceil,
    cos,
    cosh,
    db,
    derivative,
    exp,
    find,
    floor,
    imag,
    integral,
    log,
    log10,
    naverage,
    nintegral,
    nmax,
    nmin,
    phase,
    real,
    round,
    sin,
    sinh,
    sqrt,
    tan,
    tanh,
    wcomplex,
    wfloat,
    wint,
    wvalue
)
from .constants import FP_ATOL, FP_RTOL