from typing import Dict

class Agent:
    RANKS: Dict[str, int] = {
        "senior agent": 5,
        "operative": 4,
        "analyst": 3,
        "consultant": 2,
        "intern": 1
    }

    def __init__(self, name: str, position: str, age: int, gender: bool) -> None:
        self.name = name
        self.position = position
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f"{self.position} {self.name.title()}"

    def __repr__(self) -> str:
        return f"Agent(name={self.name!r}, position={self.position!r}, age={self.age!r}, gender={self.gender!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Agent):
            return False

        return (self.name == other.name and
                self.position == other.position and
                self.age == other.age and
                self.gender == other.gender)

    def get_position_weight(self) -> int:
        return self.RANKS.get(self.position, 0)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Agent):
            return NotImplemented

        return self.get_position_weight() < other.get_position_weight()