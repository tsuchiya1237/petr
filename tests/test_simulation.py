import os
import sys

# Ensure the package root is on the import path when tests are executed.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from infra_sim.simulation import run


def test_run_returns_expected_number_of_samples():
    duration = 60
    interval = 5
    data = run(duration=duration, interval=interval)
    expected = duration // interval + 1  # includes time zero
    assert len(data) == expected
