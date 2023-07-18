
__all__ = ["Chest","Crate","PlayerInventory"]


class Chest:
    def __init__(self) -> None:
        self.codename = "storage_chest"
        self.storage = []
        self.capacity = 5

class Crate:
    def __init__(self) -> None:
        self.codename = "storage_crate"
        self.storage = []
        self.capacity = 15
        


class PlayerInventory:
    def __init__(self) -> None:
        self.codename = "storage_player_inventory"
        self.storage = []
        self.capacity = 20
