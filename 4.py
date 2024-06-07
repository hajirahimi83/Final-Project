import math

# Parameters
Power = float(input("Transformer power (watts)"))               # in watts
Current_Density = float(input("Current Density (A/cm²)"))       # in A/cm²
Primary_Voltage = float(input("Primary Voltage(volts)"))        # in volts
Secondary_Voltage = float(input("Secondary Voltage(volts)"))    # in volts

# Calculation of the core cross-sectional area with four decimal places
A_core = round(Power / (Current_Density * Secondary_Voltage), 4)

# Calculation of the number of turns with four decimal places
N_primary = round(Primary_Voltage / math.sqrt(2), 4)
N_secondary = round(Secondary_Voltage / math.sqrt(2), 4)

# Print the results
print(f"Core cross-sectional area: {A_core} cm²")
print(f"Number of turns in primary coil: {N_primary}")
print(f"Number of turns in secondary coil: {N_secondary}")
import math

