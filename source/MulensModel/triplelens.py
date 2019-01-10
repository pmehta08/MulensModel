import numpy as np


class TripleLens(object):
    """
    The binary lens equation - its solutions, images, parities,
    magnifications, etc.

    Attributes :
        mass_1: *float*
            Mass of the primary as a fraction of the total mass.

        mass_2: *float*
            Mass of the secondary as a fraction of the total mass.

        mass_3: *float*
            Mass of the tertiary as a fraction of the total mass.
            NOTE - add conventions

        separation_21: *float*
            Separation between bodies 2 and 1 as a fraction of
            the Einstein ring of the whole system.

        separation_31: *float*
            Separation between bodies 2 and 1 as a fraction of
            the Einstein ring of the whole system.

        psi: *float*
            NOTE - description

    Note: masses 1, 2, and 3 may be defined as a fraction of some other
    mass than the total mass. This is possible but not recommended -
    make sure you know what you're doing before you start using this
    possibility.
    """
    def __init__(self, mass_1=None, mass_2=None, mass_3=None,
                 separation_21=None, separation_31=None, psi=None):
        self.mass_1 = mass_1
        self.mass_2 = mass_2
        self.mass_3 = mass_3
        self.separation_21 = separation_21
        self.separation_31 = separation_31
        self.psi = psi

    def point_source_magnification(self, source_x, source_y):
        """
        Calculate point source magnification for given position. The
        origin of the coordinate system is 
NOTE - the part below needs thinking and update:
#        at the center of mass and
#        both masses are on X axis with higher mass at negative X; this
#        means that the higher mass is at (X, Y)=(-s*q/(1+q), 0) and
#        the lower mass is at (s/(1+q), 0).

        Parameters :
            source_x: *float*
                X-axis coordinate of the source.

            source_y: *float*
                Y-axis coordinate of the source.

        Returns :
            magnification: *float*
                Point source magnification.
        """
        pass

    #def hexadecapole_magnification(self, source_x, source_y, rho, gamma,
                                   #quadrupole=False, all_approximations=False):
        """
        Magnification in hexadecapole approximation of the
        binary-lens/finite-source event - based on `Gould 2008 ApJ
        681, 1593
        <http://adsabs.harvard.edu/abs/2008ApJ...681.1593G>`_.

        For coordinate system convention see
        :py:func:`point_source_magnification()`

        Parameters :
            source_x: *float*
                X-axis coordinate of the source.

            source_y: *float*
                Y-axis coordinate of the source.

            rho: *float*
                Source size relative to Einstein ring radius.

            gamma: *float*
                Linear limb-darkening coefficient in gamma convention.

            quadrupole: *boolean*, optional
                Return quadrupole approximation instead of hexadecapole?
                Default is *False*.

            all_approximations: *boolean*, optional
                Return hexadecapole, quadrupole, and point source
                approximations? Default is *False*.

        Returns :
            magnification: *float* or *sequence* of three *floats*
                Hexadecapole approximation (*float*) by default.
                Quadrupole approximation (*float*) if *quadrupole*
                parameter is *True*. Hexadecapole, quadrupole, and
                point source approximations (*sequence* of three
                *floats*) if *all_approximations* parameter is *True*.
        """
