class Human:
    def __init__(self, name: str):
        self.name = name
        self.current_activity = "idle"
        self.activity_history: list[str] = []

    def _record_activity(self, activity: str, message: str) -> str:
        self.current_activity = activity
        self.activity_history.append(activity)
        return message

    def work(self) -> str:
        return self._record_activity("working", f"{self.name} is working.")

    def sleep(self) -> str:
        return self._record_activity("sleeping", f"{self.name} is sleeping.")

    def eat(self, meal: str = "a meal") -> str:
        return self._record_activity("eating", f"{self.name} is eating {meal}.")

    def play(self, game: str = "for fun") -> str:
        return self._record_activity("playing", f"{self.name} is playing {game}.")
