# test_ptypes.py
# Copyright (c) 2013-2016 Pablo Acosta-Serafini
# See LICENSE for details
# pylint: disable=C0103,C0111,W0108

# PyPI imports
import numpy
from pmisc import AE
# Intra-package imports
import peng.ptypes


###
# Global variables
###
emsg = lambda msg: (
    '[START CONTRACT MSG: {0}]Argument `*[argument_name]*` '
    'is not valid[STOP CONTRACT MSG]'.format(msg)
)


###
# Helper functions
###
def check_contract(obj, name, value):
    AE(obj, ValueError, emsg(name), obj=value)


###
# Test functions
###
def test_engineering_notation_number():
    """ Test EngineeringNotationNumber pseudo-type """
    obj = peng.ptypes.engineering_notation_number
    items = ['3.12b', 'f', 'a1b', '   +  123.45f  ']
    for item in items:
        check_contract(obj, 'engineering_notation_number', item)
    items = ['   +123.45f  ', '   -0  ']
    for item in items:
        obj(item)


def test_engineering_notation_suffix():
    """ Test EngineeringNotationSuffix pseudo-type """
    obj = peng.ptypes.engineering_notation_suffix
    check_contract(obj, 'engineering_notation_suffix', 'b')
    obj('u')


def test_increasing_real_numpy_vector_contract():
    """ Tests for IncreasingRealNumpyVector pseudo-type """
    obj = peng.ptypes.increasing_real_numpy_vector
    items = [
        'a',
        [1, 2, 3],
        numpy.array([]),
        numpy.array([[1, 2, 3], [4, 5, 6]]),
        numpy.array(['a', 'b']),
        numpy.array([1, 0, -3]),
        numpy.array([10.0, 8.0, 2.0])
    ]
    for item in items:
        check_contract(obj, 'increasing_real_numpy_vector', item)
    items = [
        numpy.array([1, 2, 3]),
        numpy.array([10.0, 12.1, 12.5]),
        numpy.array([10.0])
    ]
    for item in items:
        obj(item)


def test_number_numpy_vector_contract():
    """ Tests for NumberNumpyVector pseudo-type """
    exmsg = (
        '[START CONTRACT MSG: number_numpy_vector]Argument '
        '`*[argument_name]*` is not valid[STOP CONTRACT MSG]'
    )
    items = [
        'a',
        [1, 2, 3],
        numpy.array([]),
        numpy.array([[1, 2, 3], [4, 5, 6]]),
        numpy.array(['a', 'b']),
    ]
    for item in items:
        AE(peng.ptypes.number_numpy_vector, ValueError, exmsg, item)
    items = [
        numpy.array([1, 2, 3]),
        numpy.array([10.0, 8.0, 2.0]),
        numpy.array([10.0]),
        numpy.array([complex(1, 1), complex(2, 2)])
    ]
    for item in items:
        peng.ptypes.number_numpy_vector(item)



def test_touchstone_data_contract():
    """ Tests for TouchstoneData pseudo-type """
    obj = peng.ptypes.touchstone_data
    exmsg = (
        '[START CONTRACT MSG: touchstone_data]Argument '
        '`*[argument_name]*` is not valid'
        '[STOP CONTRACT MSG]'
    )
    freq = numpy.array([1, 2, 3])
    data = numpy.resize(numpy.arange(1, 1+(3*(2**2))), (3, 2, 2))
    wdata1 = numpy.array([1, 2, -3, 4])
    wdata2 = numpy.array([1, 'a', 3])
    wfreq1 = numpy.array([1, 2, 'a'])
    wfreq2 = numpy.array([1, 2, 3, 4])
    items = [
        45,
        {},
        {'hello':5},
        {'points':1, 'freq':2},
        {'points':1, 'freq':2, 'data':3, 'hello':4},
        {'points':'a', 'freq':freq, 'data':data},
        {'points':3, 'freq':'a', 'data':data},
        {'points':3, 'freq':freq, 'data':'a'},
        {'points':3, 'freq':data, 'data':data},
        {'points':3, 'freq':freq, 'data':wdata1},
        {'points':3, 'freq':freq, 'data':wdata2},
        {'points':3, 'freq':wfreq1, 'data':data},
        {'points':3, 'freq':wfreq2, 'data':data},
    ]
    for item in items:
        AE(obj, ValueError, exmsg, item)
    obj({'points':3, 'freq':freq, 'data':data})


def test_touchstone_noise_data_contract():
    """ Tests for TouchstoneNoiseData pseudo-type """
    obj = peng.ptypes.touchstone_noise_data
    exmsg = (
        '[START CONTRACT MSG: touchstone_noise_data]Argument '
        '`*[argument_name]*` is not valid'
        '[STOP CONTRACT MSG]'
    )
    freq = numpy.array([1, 2, 3])
    nf = numpy.array([4, 5, 6])
    rc = numpy.array([1+2j, 3+4j, 5+6j])
    res = numpy.array([50.0, 25.0, 75.0])
    wres = numpy.array([1, 2, -3])
    items = [
        45,
        {'hello':5},
        {'points':1, 'freq':2, 'nf':3, 'rc':4},
        {'points':1, 'freq':2, 'nf':3, 'rc':4, 'res':5, 'hello':2},
        {'points':1, 'freq':2, 'nf':3, 'rc':4, 'res':5, 'hello':2},
        {'points':'a', 'freq':freq, 'nf':nf, 'rc':rc, 'res':res},
        {'points':3, 'freq':'a', 'nf':nf, 'rc':rc, 'res':res},
        {'points':3, 'freq':freq, 'nf':'a', 'rc':rc, 'res':res},
        {'points':3, 'freq':freq, 'nf':nf, 'rc':'a', 'res':res},
        {'points':3, 'freq':freq, 'nf':nf, 'rc':rc, 'res':'a'},
        {'points':3, 'freq':res, 'nf':nf, 'rc':rc, 'res':res},
        {'points':3, 'freq':freq, 'nf':nf, 'rc':rc, 'res':wres},
        {'points':4, 'freq':freq, 'nf':nf, 'rc':rc, 'res':res},
    ]
    for item in items:
        AE(obj, ValueError, exmsg, item)
    obj({})
    obj({'points':3, 'freq':freq, 'nf':nf, 'rc':rc, 'res':res})


def test_touchstone_options_contract():
    """ Tests for TouchstoneOptions pseudo-type """
    obj = peng.ptypes.touchstone_options
    exmsg = (
        '[START CONTRACT MSG: touchstone_options]Argument '
        '`*[argument_name]*` is not valid'
        '[STOP CONTRACT MSG]'
    )
    items = [
        45,
        {},
        {'hello':5},
        {'units':1, 'ptype':2, 'pformat':3},
        {'units':1, 'ptype':2, 'pformat':3, 'z0':4, 'hello':5},
        {'units':'a', 'pformat':'MA', 'ptype':'S', 'z0':50.0},
        {'units':'GHz', 'pformat':'a', 'ptype':'S', 'z0':50.0},
        {'units':'GHz', 'pformat':'MA', 'ptype':'a', 'z0':50.0},
        {'units':'GHz', 'pformat':'MA', 'ptype':'S', 'z0':'a'},
        {'units':'GHz', 'pformat':'MA', 'ptype':'S', 'z0':-50.0},
    ]
    for item in items:
        AE(obj, ValueError, exmsg, item)
    obj({'units':'gHz', 'pformat':'Ri', 'ptype':'s', 'z0':50.0})


def test_wave_interp_option_contract():
    """ Tests for WaveInterpolationOption pseudo-type """
    exmsg = (
        '[START CONTRACT MSG: wave_interp_option]Argument '
        '`*[argument_name]*` is not valid'
        '[STOP CONTRACT MSG]'
    )
    items = [None, True, 'a', 5.0, []]
    for item in items:
        AE(peng.ptypes.wave_interp_option, ValueError, exmsg, item)
    items = [
            'STAIRCASE', 'CONTINUOUS',
            'staircase', 'continuous',
            'sTaiRcAsE', 'cOnTiNuOuS'
    ]
    for item in items:
        peng.ptypes.wave_interp_option(item)


def test_wave_scale_option_contract():
    """ Tests for WaveScaleOption pseudo-type """
    exmsg = (
        '[START CONTRACT MSG: wave_scale_option]Argument '
        '`*[argument_name]*` is not valid'
        '[STOP CONTRACT MSG]'
    )
    items = [None, True, 'a', 5.0, []]
    for item in items:
        AE(peng.ptypes.wave_scale_option, ValueError, exmsg, item)
    for item in ['LINEAR', 'LOG', 'linear', 'log', 'LiNeAr', 'lOg']:
        peng.ptypes.wave_scale_option(item)


def test_wave_vectors_contract():
    """ Tests for WaveVectors pseudo-type """
    exmsg = (
        '[START CONTRACT MSG: wave_vectors]Argument '
        '`*[argument_name]*` is not valid'
        '[STOP CONTRACT MSG]'
    )

    items = [
        'a',
        True,
        None,
        {},
        [],
        (None, None),
        [(None, None)],
        [(None, 1)],
        [(1, None)],
        [(1, 2, 3)],
        [(1, 100), (2, 200), (0, 300)],
        [(1, 100), (2, 200), (0, 'a')],
        [(1, 100), ('b', 200), (0, 300)],
    ]
    for item in items:
        AE(peng.ptypes.wave_vectors, ValueError, exmsg, item)
    peng.ptypes.wave_vectors([(0, 100), (1, 200), (2, 300)])