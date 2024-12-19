import polars as pl

from typing import List

import logging

logger = logging.getLogger("DataLoader")


class DataLoader:
    """
    Loads data from the data source
    """

    def __init__(
        self, conn_str: str, strategy_config: List[dict], training_config: dict
    ):
        """
        Initializes the data loader with the connection string
        """

        self.conn_str = conn_str
        self.strategy_config = strategy_config
        self.training_config = training_config
        self.result = {}
        self.start_date = training_config["forward_walk"]["start"]
        self.end_date = training_config["forward_walk"]["end"]

    def load_data(self) -> dict[str : pl.LazyFrame]:
        """
        Loads data from the data source
        """

        for config in self.strategy_config:
            for data in config["Data"]:

                table_name = data["table_name"]
                symbols = data["symbols"]

                query = f"""
                    SELECT * FROM {table_name} WHERE symbol IN {symbols} and
                    timestamp >= '{self.start_date}' and timestamp <= '{self.end_date}'
                """

                df = pl.read_sql(self.conn_str, query).load()
                self.result[
                    f"""{config["Module"]}_{config["Class"]}_{table_name}"""
                ] = df

                logger.info(
                    f"""Data loaded for {config["Module"]}_{config["Class"]}_{table_name}"""
                )
        return self.result
