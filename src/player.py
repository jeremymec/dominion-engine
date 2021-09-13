from uuid import uuid5, UUID

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.id: UUID = uuid5(name)