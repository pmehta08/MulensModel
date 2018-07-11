"""
The method should be set by the user to Model class. And then passed to 
ModelParamters. Together with it, we should pass other important information. 

The ModelParamters.__init__ has:
times, parameters, parallax=None, coords=None, satellite_skycoord=None, gamma=0.
This are used to produce:
Trajectory
and also there are methods_parameters that can be passed.

For sure we want to pass:
parameters, gamma
WHAT ELSE?
"""
import ctypes

from MulensModel import binarylens


binarylens.vbbl.VBBinaryLensing_BinaryMagDark_2.argtypes = 5 * [ctypes.c_double]
binarylens.vbbl.VBBinaryLensing_BinaryMagDark_2.restype = ctypes.c_double
# The function:
# binarylens.vbbl.VBBinaryLensing_BinaryMagDark_2 
# has following paramters:
# double s, double q, double y1v, double y2v, double rho

