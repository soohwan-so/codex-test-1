import random


def pick_random_numbers(count=20, start=1, end=100):
    """Return unique random numbers within the inclusive range."""
    population = range(start, end + 1)
    return random.sample(population, count)


def print_random_numbers():
    numbers = pick_random_numbers()
    print(" ".join(map(str, numbers)))
    return numbers


if __name__ == "__main__":
    print_random_numbers()
