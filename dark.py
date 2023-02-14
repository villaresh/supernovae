perl = resource_filename('data', 'perlmutter.txt')
dat = pd.read_csv(perl, names=['z', 'Effective magnitude'], comment='#', sep='\s+')
pl.plot(dat['z'], dat['Effective magnitude'], marker='x', color='k', lw=0.0)
# plot z-eff.magnitude
import seaborn as sns
sns.set_theme(style="whitegrid")
pl.xlabel('z')
pl.ylabel('Effective magnitude')


from astropy.cosmology import FlatLambdaCDM

def lumdist(z, olambda):
  cosmo = FlatLambdaCDM(H0=70, Om0=1. - olambda, Tcmb0=2.725)
    
  return  cosmo.luminosity_distance(z) 

# We then need to convert this distance into how astronomers measure brightness
def effmag(z, olambda, MB):
  DL = lumdist(z, olambda)   

  return MB + 5. * np.log10(DL.value) 

# First plot poster
zs = np.arange(0.01, 0.85, 0.01)

pl.plot(dat['z'], dat['Effective magnitude'], marker='x', color='k', lw=0.0)

pl.plot(zs, effmag(zs, 0.0, 6.), c='k', label='No Dark Energy', linestyle='--',alpha=0.4)
pl.plot(zs, effmag(zs, 0.4, 6.), c='k', label='50% Dark Energy',linestyle='-.',alpha=0.6)
pl.plot(zs, effmag(zs, 0.75, 6.), c='k', label='75% Dark Energy',linestyle='-.')

pl.xlabel('z')
pl.ylabel('Effective magnitude')

pl.legend(loc=4, frameon=False)

#####################################
from scipy.optimize import minimize
def chi2(x):
     olambda = x[0]
     MB      = x[1] 
    
     model   = effmag(dat['z'], olambda, MB) 
     
     return  np.sum((dat['Effective magnitude'] - model)**2.) 
    
res = minimize(chi2, x0=[0.5, 5.0], options={'disp': True})
res.x

########################3
# Plot trend line
pl.plot(dat['z'], dat['Effective magnitude'], marker='x', color='k', lw=0.0)

pl.xlabel('z')
pl.ylabel('Effective magnitude')

#calculate equation for quartic trendline
z = np.polyfit(dat['z'],dat['Effective magnitude'] , 4)
p = np.poly1d(z)

seq = [0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.30,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.40,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.50,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.837]
#add trendline to plot
plt.plot(seq, p(seq), 'darkslategrey', label='Trend line')
pl.legend(loc=4, frameon=False)
