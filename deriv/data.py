import configparser

class Config:
        
    def __init__(self,
                 market: dict = None,
                 contract: dict = None):
        
        self.market = market
        self.contract = contract

    @classmethod
    def load(cls,
             configfile: str):
        
        obj = cls()
        config = configparser.ConfigParser()
        config.read_file(open(configfile))
        obj.market = {key: float(value) for key, value in dict(config.items("Market")).items()}
        obj.contract = {key: float(value) for key, value in dict(config.items("Contract")).items()}
        return obj
