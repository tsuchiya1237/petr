"""Environment models for infrastructure sensor simulation."""
from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass
class TemperatureEnvironment:
    """Simple ambient temperature model.

    The model uses a sinusoidal daily cycle plus Gaussian noise.

    Attributes:
        base: Average temperature in degrees Celsius.
        amplitude: Amplitude of the daily temperature variation.
        period: Period of the sinusoid in minutes (default: one day).
        noise_std: Standard deviation of the random noise.
    """

    base: float = 20.0
    amplitude: float = 5.0
    period: float = 24 * 60.0
    noise_std: float = 0.5

    def temperature(self, time_min: float) -> float:
        """Return the environment temperature at a given simulation time."""
        # Deterministic sinusoidal component
        deterministic = self.base + self.amplitude * math.sin(
            2 * math.pi * (time_min % self.period) / self.period
        )
        # Random noise component
        noise = random.gauss(0.0, self.noise_std)
        return deterministic + noise
