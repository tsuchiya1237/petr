"""Sensor models for infrastructure simulation."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from .environment import TemperatureEnvironment


@dataclass
class TemperatureSensor:
    """A simple temperature sensor that samples the environment.

    The sensor periodically queries the attached environment. Samples are
    stored in ``data`` as tuples of ``(time, value)``.
    """

    environment: TemperatureEnvironment
    interval: float = 1.0
    data: List[Tuple[float, float]] = field(default_factory=list)

    def run(self, duration: float) -> List[Tuple[float, float]]:
        """Collect measurements for the given duration."""
        time = 0.0
        while time <= duration:
            temp = self.environment.temperature(time)
            self.data.append((time, temp))
            time += self.interval
        return self.data
