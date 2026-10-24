def main():
    mass = int(input("Enter the mass of the object in kilograms: "))
    print(f"The energy is: {calculate_energy(mass)} joules")


def calculate_energy(mass):
    c = 3e08  # speed of light in meters per second
    energy = mass * c ** 2
    return energy

main()