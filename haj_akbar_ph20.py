#ideal gas law!!
from typing import _ProtocolMeta


pascal = 20000000
volume = 12
gas_constant = 8.314
temerature = (20 + 273.15)
mol = ((pascal * volume) / (gas_constant * temerature))
print("mol :" , mol)