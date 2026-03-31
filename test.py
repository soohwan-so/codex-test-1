import io
import unittest
from contextlib import redirect_stdout

from human import Human
from human_manager import HumanManager
from main import build_manager, pick_random_numbers, print_random_numbers, run_manager_demo


class RandomNumberTests(unittest.TestCase):
    def test_pick_random_numbers_returns_20_unique_values_in_range(self):
        numbers = pick_random_numbers()

        self.assertEqual(len(numbers), 20)
        self.assertEqual(len(set(numbers)), 20)
        self.assertTrue(all(1 <= number <= 100 for number in numbers))

    def test_print_random_numbers_prints_generated_values(self):
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            numbers = print_random_numbers()

        printed_numbers = [int(value) for value in buffer.getvalue().strip().split()]
        self.assertEqual(printed_numbers, numbers)


class HumanTests(unittest.TestCase):
    def test_human_can_work_sleep_eat_and_play(self):
        human = Human("Alice")

        self.assertEqual(human.work(), "Alice is working.")
        self.assertEqual(human.sleep(), "Alice is sleeping.")
        self.assertEqual(human.eat("lunch"), "Alice is eating lunch.")
        self.assertEqual(human.play("soccer"), "Alice is playing soccer.")
        self.assertEqual(
            human.activity_history,
            ["working", "sleeping", "eating", "playing"],
        )


class HumanManagerTests(unittest.TestCase):
    def test_manager_can_manage_humans(self):
        manager = HumanManager("Bob")
        human = Human("Alice")

        self.assertEqual(manager.add_human(human), "Bob now manages Alice.")
        self.assertEqual(manager.manage(), "Bob is managing Alice.")
        self.assertEqual(manager.current_activity, "managing")

    def test_manager_can_assign_activity_to_managed_human(self):
        manager = HumanManager("Bob")
        human = Human("Alice")
        manager.add_human(human)

        result = manager.assign_activity("Alice", "eat", "dinner")

        self.assertEqual(result, "Alice is eating dinner.")
        self.assertEqual(human.current_activity, "eating")

    def test_manager_cannot_manage_themselves(self):
        manager = HumanManager("Bob")

        with self.assertRaises(ValueError):
            manager.add_human(manager)


class MainTests(unittest.TestCase):
    def test_build_manager_creates_one_manager_with_team(self):
        manager = build_manager()

        self.assertIsInstance(manager, HumanManager)
        self.assertEqual(manager.name, "Bob")
        self.assertEqual([human.name for human in manager.team], ["Alice", "Charlie"])

    def test_run_manager_demo_prints_management_flow(self):
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            events = run_manager_demo()

        self.assertEqual(
            events,
            [
                "Bob is managing Alice, Charlie.",
                "Alice is working.",
                "Charlie is eating lunch.",
                "Charlie is playing chess.",
            ],
        )
        self.assertEqual(buffer.getvalue().strip().splitlines(), events)


if __name__ == "__main__":
    unittest.main()
