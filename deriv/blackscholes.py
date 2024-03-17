from dataclasses import dataclass

@dataclass
class Market:
    spot: float
    rd: float
    rf: float
    vol: float


@dataclass
class Contract:
    strike: float
    T: float
    phi: int
    notional: float

class Vanilla:

    pass

class MonteCarlo:

    
    def __init__(self):
        pass

    def _simulate(self,
                  n_sim: int,
                  func: function):
        pass

    def evaluate(self):
        """
        Calculate the average of the simulations.
        """

    def metrics(self,
                conf: float):
        """
        Return the ST DEV of the estimates.
        """