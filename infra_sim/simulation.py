"""Top level simulation utilities."""
from __future__ import annotations

from typing import List, Tuple

from .environment import TemperatureEnvironment
from .sensor import TemperatureSensor


def run(duration: float = 60.0, interval: float = 5.0) -> List[Tuple[float, float]]:
    """Run a temperature sensor simulation.

    Args:
        duration: Total duration of the simulation in minutes.
        interval: Sampling interval of the sensor in minutes.
    Returns:
        List of ``(time, value)`` samples produced by the sensor.
    """
    temp_env = TemperatureEnvironment()
    sensor = TemperatureSensor(temp_env, interval=interval)
    return sensor.run(duration)


if __name__ == "__main__":  # pragma: no cover - manual run helper
    readings = run(240.0, interval=10.0)
    for t, value in readings:
        print(f"{t:5.1f} min : {value:.2f} C")
