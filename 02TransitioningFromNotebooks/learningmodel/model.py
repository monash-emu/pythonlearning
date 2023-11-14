from datetime import datetime

from summer2 import CompartmentalModel
from summer2.parameters import Parameter as param
from summer2.utils import Epoch

from .helpers import get_seed_function


REF_DATE = datetime(2019, 1, 1)


def build_model():
    m = CompartmentalModel([0, 100], ["S", "I", "R"], "I", ref_date=REF_DATE)

    m.set_initial_population({"S": 1000.0})

    # Seed at seed_rate, from a parameterised start time, for a fixed length of 7 days
    seed_func = get_seed_function(param("seed_start"), 7.0, param("seed_rate"))

    m.add_importation_flow("seed", seed_func, "I", split_imports=True)

    m.add_infection_frequency_flow("infection", param("contact_rate"), "S", "I")
    m.add_transition_flow("recovery", param("recovery_rate"), "I", "R")

    m.request_output_for_flow("infection", "infection")

    for c in ["S", "I", "R"]:
        m.request_output_for_compartments(c, c)

    return m


DEFAULT_PARAMS = {
    "seed_start": Epoch(REF_DATE).datetime_to_number(datetime(2019, 2, 1)),
    "seed_rate": 2.0,
    "contact_rate": 0.4,
    "recovery_rate": 0.1,
}
