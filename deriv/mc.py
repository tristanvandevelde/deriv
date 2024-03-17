import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from mm.data import Config
from mm.process import Process, BlackScholes


class MonteCarlo:

    """
    Generic class to perform risk-neutral option pricing through Monte Carlo simulations.
    """

    def __init__(self,
                 config: Config = None,
                 process: Process = None,
                 seed: int = None):
        
        self.market = config.market
        self.contract = config.contract
        self.process = process
        self.seed = seed

        if seed is not None:
            np.random.seed(seed)

        self.disc = np.exp(-1 * self.market["rd"] * self.contract["t"])
        

    def simulate(self,
                n_sim=1_000):
        
        z = np.random.normal(0, 1, n_sim)
        self._sim = self.process.project(self.market, self.contract, z)
    

    def evaluate(self,
                 n_sim=1_000):
        
        self.simulate(n_sim)
        payoff = np.maximum(0, self.contract["phi"] * (self._sim - self.contract["strike"]))
        self.price = self.disc * np.average(payoff)
    


    def hist(self):

        try:
            self._sim
        except:
            self.simulate()

        plt.hist(self.market["spot"] * self._sim, bins=50)
        plt.show()