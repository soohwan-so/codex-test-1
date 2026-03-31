import random

from human import Human
from human_manager import HumanManager


def pick_random_numbers(count=20, start=1, end=100):
    """Return unique random numbers within the inclusive range."""
    population = range(start, end + 1)
    return random.sample(population, count)


def print_random_numbers():
    numbers = pick_random_numbers()
    print(" ".join(map(str, numbers)))
    return numbers


def build_manager() -> HumanManager:
    manager = HumanManager("Bob")
    manager.add_human(Human("Alice"))
    manager.add_human(Human("Charlie"))
    return manager


def run_manager_demo() -> list[str]:
    manager = build_manager()
    events = [
        manager.manage(),
        manager.assign_activity("Alice", "work"),
        manager.assign_activity("Charlie", "eat", "lunch"),
        manager.assign_activity("Charlie", "play", "chess"),
    ]

    for event in events:
        print(event)

    return events


if __name__ == "__main__":
    run_manager_demo()
