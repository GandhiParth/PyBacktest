from datetime import datetime


class Risk:
    def __init__(self, conf: dict):
        self.conf = conf

    def validate_trade(
        self,
        strategy: str,
        signal: int,
        symbol: str,
        price: float,
        quantity: int,
        timestamp: datetime,
    ):
        pass
