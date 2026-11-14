#!/usr/bin/env python3
"""Make a small QCoDeS database with simulated instruments, for testing the reader.

Needs QCoDeS (pip install qcodes). Writes three runs on a pretend device "D7":
  1. gate sweep at 12 mK, 0 T, completed
  2. gate sweep at 0.5 T, aborted after 40 points (simulates a crash)
  3. gate sweep at 0.5 T, lock-in time constant changed, completed

  python3 make_test_db.py OUT.db
"""
import sys

import numpy as np
import qcodes as qc
from qcodes.dataset import Measurement, initialise_or_create_database_at, load_or_create_experiment
from qcodes.instrument import Instrument
from qcodes.parameters import Parameter


class Fake(Instrument):
    pass


def main(path):
    initialise_or_create_database_at(path)
    exp = load_or_create_experiment("cooldown3", sample_name="D7")

    fridge = Fake("fridge")
    fridge.add_parameter("T_mc", unit="K", initial_value=0.012, set_cmd=None, get_cmd=None)
    magnet = Fake("magnet")
    magnet.add_parameter("B", unit="T", initial_value=0.0, set_cmd=None, get_cmd=None)
    lockin = Fake("lockin")
    lockin.add_parameter("time_constant", unit="s", initial_value=0.1, set_cmd=None, get_cmd=None)
    lockin.add_parameter("amplitude", unit="V", initial_value=0.01, set_cmd=None, get_cmd=None)
    dac = Fake("dac")
    dac.add_parameter("gate", unit="V", initial_value=0.0, set_cmd=None, get_cmd=None)
    g = Parameter("G", unit="e^2/h", get_cmd=lambda: float(np.exp(dac.gate() / 0.5)), instrument=None)

    station = qc.Station(fridge, magnet, lockin, dac)

    def sweep(name, n, abort_at=None):
        meas = Measurement(exp=exp, station=station, name=name)
        meas.register_parameter(dac.gate)
        meas.register_parameter(g, setpoints=(dac.gate,))
        try:
            with meas.run() as ds:
                for i, v in enumerate(np.linspace(-2, 0.5, n)):
                    if abort_at is not None and i == abort_at:
                        raise RuntimeError("simulated crash: lost contact to the DAC")
                    dac.gate(v)
                    ds.add_result((dac.gate, v), (g, g()))
        except RuntimeError as e:
            print("run aborted as planned:", e)

    sweep("gate_sweep", 101)
    magnet.B(0.5)
    sweep("gate_sweep", 101, abort_at=40)
    lockin.time_constant(0.3)
    sweep("gate_sweep", 101)
    print("wrote", path)


if __name__ == "__main__":
    main(sys.argv[1])
