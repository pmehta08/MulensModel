#! /usr/bin/env python

import sys
import numpy as np
import unittest
from astropy.time import Time

from MulensModel.model import Model
from MulensModel.modelparameters import ModelParameters
from MulensModel.mulensdata import MulensData


def test_model_PSPL_1():
    """tests basic evaluation of Paczynski model"""
    t_0 = 5379.57091
    u_0 = 0.52298
    t_E = 17.94002
    times = np.array([t_0-2.5*t_E, t_0, t_0+t_E])
    data = MulensData(data_list=[times, times*0., times*0.], date_fmt='jdprime')
    model = Model(t_0=t_0, u_0=u_0, t_E=t_E)
    model.u_0 = u_0
    model.t_E = t_E
    model.set_datasets([data])
    np.testing.assert_almost_equal(model.magnification, [
            np.array([1.028720763, 2.10290259, 1.26317278])], 
            err_msg="PSPL model returns wrong values")

def test_model_init_1():
    """tests if basic parameters of Model.__init__() are properly passed"""
    t_0 = 5432.10987
    u_0 = 0.001
    t_E = 123.456
    rho = 0.0123
    m = Model(t_0=t_0, u_0=u_0, t_E=t_E, rho=rho)
    np.testing.assert_almost_equal(m.t_0, t_0, err_msg='t_0 not set properly')
    np.testing.assert_almost_equal(m.u_0, u_0, err_msg='u_0 not set properly')
    np.testing.assert_almost_equal(m.t_E, t_E, err_msg='t_E not set properly')
    np.testing.assert_almost_equal(m.rho, rho, err_msg='rho not set properly')

class TestModel(unittest.TestCase):
    def test_negative_t_E(self):
        with self.assertRaises(ValueError):
            m = Model(t_E=-100.)

class TestModelParallax(unittest.TestCase):
    def test_too_many_parameters_for_init(self):
        with self.assertRaises(ValueError):
            mp = ModelParameters(pi_E=(1., 1.), pi_E_N=1.)
        with self.assertRaises(ValueError):
            mp = ModelParameters(pi_E=(1., 1.), pi_E_E=1.)

def test_model_parallax_definition():
    model_1 = Model()
    model_1.pi_E = (0.1,0.2)
    assert model_1.pi_E_N == 0.1
    assert model_1.pi_E_E == 0.2

    model_2 = Model()
    model_2.pi_E_N = 0.3
    model_2.pi_E_E = 0.4
    assert model_2.pi_E_N == 0.3
    assert model_2.pi_E_E == 0.4

    model_3 = Model(pi_E=(0.5,0.6))
    assert model_3.pi_E_N == 0.5
    assert model_3.pi_E_E == 0.6

    model_4 = Model(pi_E_N=0.7, pi_E_E=0.8)
    assert model_4.pi_E_N == 0.7
    assert model_4.pi_E_E == 0.8

"""
This is a high-level unit test for parallax. The "true" values were calculated from the sfit routine assuming fs=1.0, fb=0.0.
"""
def test_annual_parallax_calculation():
    t_0 = 7479.5 #April 1 2016, a time when parallax is large
    times = np.array([t_0-1., t_0, t_0+1.])
    true_no_par = np.array([7.12399067,10.0374609, 7.12399067])
    true_with_par = np.array([7.12376832, 10.0386009, 7.13323363])

    model_with_par = Model(t_0=t_0, u_0=0.1,t_E=10.,pi_E=(0.3,0.5),
                  coords='17:57:05 -30:22:59')
    model_with_par.parallax(satellite=False,earth_orbital=True,
                            topocentric=False)
    model_with_par.t_0_par = 7479.
    model_with_par.time = times
    
    model_no_par = Model(t_0=t_0, u_0=0.1,t_E=10.,pi_E=(0.3,0.5),
                  coords='17:57:05 -30:22:59')
    model_no_par.parallax(satellite=False,earth_orbital=False,topocentric=False)
    model_no_par.time = times
    
    np.testing.assert_almost_equal(model_no_par.magnification, true_no_par)
    np.testing.assert_almost_equal(model_with_par.magnification, true_with_par)