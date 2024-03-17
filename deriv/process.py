import numpy as np

class Process:

    def __init__(self):
        pass

    def project(self,
                market: dict):
        """
        This is a function which projects the value of an asset forward,
        given an input of a random sample.
        For this it needs to make use of a Market dict.
        """

class BlackScholes(Process):

    def project(self,
                market: dict,
                contract: dict,
                z: float):
        
        return market["spot"] * np.exp((market["rd"] - market["rf"] - (0.5 * np.power(market["sigma"], 2))) * contract["t"]) + (market["sigma"] * np.sqrt(contract["t"]) * z)