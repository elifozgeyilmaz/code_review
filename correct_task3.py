# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

"""
def average_valid_measurements(values):
    total = 0
    count = len(values)

    for v in values:
        if v is not None:
            total += float(v)

    return total / count

"""
"""
    Average numeric measurements, ignoring missing/invalid values.

    - Ignores None.
    - Accepts values convertible to float.
    - Ignores NaN and +/-inf after conversion.
    - Returns None if no valid measurements exist.
"""
from __future__ import annotations

from typing import Iterable, Any, Optional
import math


def average_valid_measurements(values: Iterable[Any]) -> Optional[float]:
   
    total = 0.0
    valid_count = 0

    for v in values:
        if v is None:
            continue
        try:
            x = float(v)
        except (TypeError, ValueError):
            continue

        if not math.isfinite(x):
            continue

        total += x
        valid_count += 1

    if valid_count == 0:
        return None

    return total / valid_count
