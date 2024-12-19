from datetime import datetime
import logging

logger = logging.getLogger("Portfolio")


class Portfolio:
    def __init__(self, initial_cash: float):

        self.intial_cash = initial_cash
        self.cash_balance = initial_cash
        self.positions = {}
        self.trade_log = []

    def execute_trade(
        self,
        strategy: str,
        signal: int,
        symbol: str,
        price: float,
        quantity: int,
        timestamp: datetime,
    ):
        """
        Executes a trade for the given symbol
        """

        if signal == 0:
            logger.info(f"No signal for {symbol} at {timestamp}")
            return
        elif signal == 1:
            cost = price * quantity
            if cost <= self.cash_balance:
                self.cash_balance -= cost
                if symbol in self.positions:
                    self.positions[symbol] += quantity
                else:
                    self.positions[symbol] = quantity
                self.trade_log.append(
                    {
                        "strategy": strategy,
                        "symbol": symbol,
                        "timestamp": timestamp,
                        "price": price,
                        "quantity": quantity,
                        "signal": signal,
                    }
                )
            else:
                logger.info(
                    f"""Not enough cash to buy {quantity} shares of {symbol} at {price} at time {timestamp}"""
                )
        elif signal == -1:
            if symbol in self.positions and self.positions[symbol] >= quantity:
                self.cash_balance += price * quantity
                self.positions[symbol] -= quantity
                if self.positions[symbol] == 0:
                    del self.positions[symbol]
                self.trade_log.append(
                    {
                        "strategy": strategy,
                        "symbol": symbol,
                        "timestamp": timestamp,
                        "price": price,
                        "quantity": quantity,
                        "signal": signal,
                    }
                )
            else:
                logger.info(f"""Not enough shares of {symbol} to sell.""")
        else:
            logger.info(f"""Invalid Signal for {symbol} : {signal}""")

    def get_summary(self) -> dict:
        """
        Return portfolio summary
        """

        return {
            "cash_balance": self.cash_balance,
            "positions": self.positions,
            "trade_log": self.trade_log,
        }

    def get_trade_price(self) -> float:
        pass

    def get_trade_quantity(self) -> int:
        pass
