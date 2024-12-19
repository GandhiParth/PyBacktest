conf = {}

conf["forward_walk"] = {
    "start": "2010-01-01",  # YYYY-MM-DD
    "end": "2012-01-01",
    "inital_cash": 1_000_000,
}

conf["risk"] = {
    "position_sizing": {
        "enabled": True,
        "percent": 0.05,
    },
    "max_position_size": {
        "enabled": True,
        "percent": 0.05,
    },
    "max_drawdown": {
        "enabled": True,
        "percent": 0.05,
    },
    "max_risk_per_trade": {
        "enabled": True,
        "percent": 0.05,
    },
    "max_exporsure": {
        "enabled": True,
        "percent": 0.05,
    },
}

conf["optuna"] = {
    "n_trials": 100,
    "n_jobs": 1,
    "timeout": 600,
    "study_name": "optuna_study",
    "objective": ["return", "sharpe", "sortino"],
    "direction": ["maximize", "maximize", "maximize"],
    "storage": "sqlite:///optuna.db",
    "sampler": "TPESampler",
    "pruner": "SuccessiveHalvingPruner",
    "pruner_params": {
        "min_resource": 1,
        "reduction_factor": 4,
        "min_early_stopping_rate": 0,
    },
    "study_params": {
        "load_if_exists": True,
    },
}
