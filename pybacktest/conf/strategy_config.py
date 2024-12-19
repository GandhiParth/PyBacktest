config = {
    "Name": "StrategyName",
    "Module": "strategy_module",
    "Class": "Strategy",
    "Frequency": "10m",  # can be added as seconds, minutes, hours etc. The frequency to fetch the data
    "Data": [
        {"table_name": "table_name", "symbols": ["ONGC", "DMART"]},
        {"table_name": "table_name", "symbols": ["TCS", "DMART"]},
    ],
}
