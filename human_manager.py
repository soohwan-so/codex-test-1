from human import Human


class HumanManager(Human):
    def __init__(self, name: str):
        super().__init__(name)
        self.team: list[Human] = []

    def add_human(self, human: Human) -> str:
        if human is self:
            raise ValueError("A manager cannot manage themselves.")

        if human not in self.team:
            self.team.append(human)

        return f"{self.name} now manages {human.name}."

    def remove_human(self, human: Human) -> str:
        if human not in self.team:
            raise ValueError(f"{human.name} is not managed by {self.name}.")

        self.team.remove(human)
        return f"{self.name} no longer manages {human.name}."

    def manage(self) -> str:
        if not self.team:
            return self._record_activity("managing", f"{self.name} has no humans to manage.")

        names = ", ".join(human.name for human in self.team)
        return self._record_activity("managing", f"{self.name} is managing {names}.")

    def get_human(self, name: str) -> Human:
        for human in self.team:
            if human.name == name:
                return human

        raise ValueError(f"No human named {name} is managed by {self.name}.")

    def assign_activity(self, name: str, activity: str, *args, **kwargs) -> str:
        human = self.get_human(name)
        action = getattr(human, activity, None)

        if not callable(action):
            raise ValueError(f"{activity} is not a valid activity for {human.name}.")

        return action(*args, **kwargs)
