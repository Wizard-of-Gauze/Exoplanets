# Exoplanets
This code uses the lightkurve module to access data from the Kepler telescope.
Lightcurves are plotted, followed by a Lomb-Scargle periodogram.
The orbital period is calculated from the frequency at max power in the periodogram.
The phase folding plot is used to determine the true orbital period as an integer multiple of the calculated period.
