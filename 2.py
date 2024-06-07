import numpy as np

def calculate_electric_field(array):
    # Constants
    k = 8.99e9  # Coulomb's constant in N m^2/C^2

    # Initialize electric field components
    Ex, Ey = 0, 0

    # Iterate through the array
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] != 'O':
                # Calculate distance from point (i, j) to point O
                r = np.sqrt((i - len(array) // 2) ** 2 + (j - len(array[0]) // 2) ** 2)

                # Calculate electric field contribution
                Q = float(array[i][j])  # Charge at point (i, j)
                dEx = k * Q * (i - len(array) // 2) / r**3
                dEy = k * Q * (j - len(array[0]) // 2) / r**3

                # Accumulate contributions
                Ex += dEx
                Ey += dEy

    return [Ex, Ey]

# Example usage
playing_field = [
    ['O', '1', 'O'],
    ['2', 'O', '3'],
    ['O', '4', 'O']
]

electric_field_at_O = calculate_electric_field(playing_field)
print(f"Electric field at point O: Ex = {electric_field_at_O[0]:.2e} N/C, Ey = {electric_field_at_O[1]:.2e} N/C")
