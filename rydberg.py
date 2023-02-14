
import pylab as pl
import numpy as np
from tools import pubplot
from tools.wave2rgb import wavelength_to_rgb
# Energy levels of Hydrogen are quantized, with electrons habitating a series of shells with discrete energies
# Light is emitted when an electron transitions between any two levels with a wavelength given by the Rydberg formula
# Definition of this formula
def Rydberg(n, m):
    formula = 1.096e-2 * (1. / n / n - 1. / m / m)
    return 1. / formula
 # We caculate the wavelengths that Hydrogen can emit
waves = []

print('n \t m \t Wavelength [nm]')

for n in np.arange(1, 10, 1):
    for m in np.arange(n+1, 10, 1):
        wave = Rydberg(n, m)        
        waves.append(wave)
        
        print('{:d} \t {:d} \t {:.3f}'.format(n, m, wave))
# If the hydrogen exists in a galaxy that is moving, we see the lines Doppler shifted
# We can calculate the redshit zc=v (the velocity v<<c, which is nearly always true, then it works)
# If we say the galaxy is moving at 1% the speed of light (v = 0.01c), the redshift is: zc = 0.01c --> z = 0.01
z1 = redshift(0.01) #shift distance

for restwave in waves:
  obswave = (1. + z1) * restwave     

  color   = wavelength_to_rgb(restwave)       
  pl.axvline(x=restwave, c=color, alpha=0.25)

  color   = wavelength_to_rgb(obswave)       
  pl.axvline(x=obswave, c=color)

pl.xlabel('Vacuum wavelength [nanometers]')
pl.xlim(380., 780.)
