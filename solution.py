import pandas as pd
import numpy as np


chat_id = 396317433 

def solution(x: np.array) -> float:
    return 2 * x.mean() / (52*52)
