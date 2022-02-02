from platform import processor, machine, system, version

print(machine(), processor(), system(), version())

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)