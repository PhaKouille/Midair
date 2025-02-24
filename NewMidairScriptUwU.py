import math
from art import *
import sys
import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def main():
    print(BLUE)
    tprint("midair")
    print(RESET)

    def input_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print(RED + "Invalide" + RESET)

    def input_int(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print(RED + "Invalide" + RESET)

    def input_axe(prompt):
        while True:
            axe = input(prompt).lower()
            if axe in ['x', 'z']:
                return axe
            else:
                print(YELLOW + "'x' ou 'z'" + RESET)

    powerX = input_float(RED + "Power x : ")
    powerY = input_float(RED + "Power y : ")
    powerZ = input_float(RED + "Power z : ")

    projX = input_float(RED + "Projectile x : ")
    projY = input_float(RED + "Projectile y : ")
    projZ = input_float(RED + "Projectile z : ")

    axe = input_axe(RED + "Axe(x,z) : ")

    power_amount = input_int(RED + "Power limite : ")
    ticks = input_int(RED + "Gametick limite : ")
    
    

    print("")

    deltaX = projX - powerX
    deltaY = projY - powerY
    deltaZ = projZ - powerZ

    distance = math.sqrt(deltaX * deltaX + deltaY * deltaY + deltaZ * deltaZ)

    x_efficiency = deltaX / distance
    z_efficiency = deltaZ / distance
    distance_efficiency = 1.0 - distance / 8

    def calculate_range(efficiency, proj, power_amount, ticks):
        goumtick = 0
        previous_positions = []

        for i in range(power_amount + 1):
            range_value = efficiency * distance_efficiency * i
            range_total = range_value + proj

            for j in range(ticks):  
                if j > 0:  
                    range_value *= 0.9800000190734863
                    range_total += range_value

                if len(previous_positions) >= 5:
                    previous_positions.pop(0)  
                previous_positions.append((i, j + 1, range_total))

                if 0.49 <= range_total % 1 <= 0.51:

                    current_power, current_tick, current_position = previous_positions[-1]
                    print(GREEN + f"Power : {current_power} | Gametick : {current_tick} | Position : {current_position}" + RESET)

                    for pwr, tick, pos in previous_positions[:-1]:
                        adjusted_power = pwr
                        adjusted_position = pos

                        while adjusted_position <= current_position:
                            adjusted_power += 1
                            range_value = efficiency * distance_efficiency * adjusted_power
                            adjusted_position = range_value + proj

                            for tick_offset in range(tick):
                                range_value *= 0.9800000190734863
                                adjusted_position += range_value
                        if current_tick >= tick:
                            
                            print(BLUE + f"Power hammer: {adjusted_power} | gameticks : {tick} | Position : {adjusted_position}" + RESET)


    if axe == "z":
        calculate_range(z_efficiency, projZ, power_amount, ticks)
    elif axe == "x":
        calculate_range(x_efficiency, projX, power_amount, ticks)

while True:
    main()
    repeat = input(YELLOW + "\nencore ? (Y/N) : " + RESET).strip().lower()
    if repeat == 'n':
        break

time.sleep(1)
sys.exit()
