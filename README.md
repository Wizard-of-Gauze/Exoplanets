# Exoplanets
This code uses the lightkurve module to access data from the Kepler telescope.
Lightcurves are plotted, followed by a Box Least Squares periodogram.
The orbital period is calculated from the frequency at max power in the periodogram.
The phase folding plot is used to determine the true orbital period as an integer multiple of the calculated period.

There is also a real time orbit simulation using pygame.
It is initialized for the solar-system, but values can be adjusted to simulate the orbits of any system.
The fourth order Runge-Kutta method is used to approximate the orbits.
