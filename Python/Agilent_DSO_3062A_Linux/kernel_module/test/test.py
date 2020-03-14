try : import pyvisa
except ImportError: print("python3 -m pip install pyvisa")

from subprocess import Popen, PIPE

rm = pyvisa.ResourceManager()
siggen = rm.get_instrument("GPIB1::19")
siggen.write("OUTP:STAT ON")