from pathlib import Path

import pandas as pd
from summer2.functions import time as stf


DATA_PATH = Path(__file__).parent / "data"


def get_seed_function(seed_start, seed_duration, seed_rate):
    return stf.get_piecewise_function(
        [seed_start, seed_start + seed_duration], [0.0, seed_rate, 0.0]
    )


def load_infection_data():
    return pd.read_csv(
        DATA_PATH / "infections.csv", parse_dates=["date"], index_col="date"
    )["infection"]
