
__all__=["AbandonedHouse","Village"]



class AbandonedHouse:
    def __init__(self) -> None:
        self.codename = "structure_abandoned_house"
        self.name = "Заброшенный Дом"
        self.storages_generated = False
        self.storages = []
        self.npcs = []

class Village:
    def __init__(self) -> None:
        self.codename = "structure_village"
        self.name = "Заброшенный Дом"
        self.storages_generated = False
        self.storages = []
        self.npcs = []

