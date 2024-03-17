
import numpy as np
from scipy import stats
import math

spot = 1.07
rd = 0.0525
rf = 0.0372
vol = 0.06
strike = 1.12
T = 0.5
phi = 1
lbd = 2
sigma_Y = 0.3
mu_Y = 0.1

def calc_jump(spot,
              rd,
              rf,
              vol,
              strike,
              T,
              phi,
              lbd,
              sigma_Y,
              mu_Y):
    Egamma = np.exp(mu_Y + (0.5 * np.power(sigma_Y, 2))) - 1    # ok
    fwd = spot * np.exp((rd - rf - (lbd * Egamma)) * T)         # ok
    lmb_p = lbd * np.exp(mu_Y + 0.5*(np.power(sigma_Y, 2)))

    #n = 0
    #dev = (0.5 * T * np.power(vol, 2)) + (0.5 * n * np.power(sigma_Y,2))
    #dplus = (np.log(fwd/strike) + n*Egamma + dev) / np.sqrt((T * np.power(vol, 2)) + (n * np.power(sigma_Y, 2)))
    #dmin = (np.log(fwd/strike) + n*Egamma - dev) / np.sqrt((T * np.power(vol, 2)) + (n * np.power(sigma_Y, 2)))
    #cf = (fwd * np.exp(n * Egamma) * stats.norm.cdf(dplus)) - (strike * stats.norm.cdf(dmin))
    #print(cf)
    #scaling = (np.exp(-1 * lmb_p * T) * np.power(lmb_p * T, n)) / math.factorial(n)
    #print(scaling)
    #print(cf*scaling)

    
    v = 0
    for n in range(0, 42+1):
        den = np.sqrt(np.power(vol,2)*T + np.power(sigma_Y,2)*n)
        var = ((0.5 * T * np.power(vol, 2)) + (0.5 * n * np.power(sigma_Y,2)))
        dplus = (np.log(fwd/strike) + n*Egamma + var) / den
        dmin = (np.log(fwd/strike) + n*Egamma - var) / den
        fact1 = ((fwd * np.exp(n * Egamma) * stats.norm.cdf(dplus)) - strike * stats.norm.cdf(dmin))
        scaling = (np.exp(-1 * lmb_p * T) * np.power(lmb_p * T, n)) / math.factorial(n) # ok
        final = fact1*scaling
        v += final

    return np.exp(-1 * rd * T) * v

v = calc_jump(spot, rd, rf, vol, strike, T, phi, lbd, sigma_Y, mu_Y)
print(v)
# lambda_der = lambda * Exp(mu_Y + (sigma_Y * sigma_Y * 0.5))
# scaling = Exp(-lambda_der * T) * (lambda_der * T) ' this is the poisson weight