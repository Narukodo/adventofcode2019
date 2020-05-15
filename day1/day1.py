from pathlib import Path
import math

def calc_fuel(mass):
    fuel = math.floor(mass/3) - 2
    total_fuel = fuel
    while fuel > 5:
        fuel = math.floor(fuel/3) - 2
        total_fuel += fuel
    return total_fuel


with open(Path(__file__).parent / 'p1.input') as inputs:
    total_mass_p2 = 0
    total_mass_p1 = 0
    for mass in inputs:
        total_mass_p1 += math.floor(int(mass)/3) - 2
        total_mass_p2 += calc_fuel(int(mass))

print(total_mass_p1)
print(total_mass_p2)
