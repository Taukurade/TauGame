
__all__ = ["Pig","Cow","Chicken","Spider","Wolf","Trader"]

class Pig:
    def __init__(self) -> None:
        self.codename = "npc_pig"
        self.name = "Свинка"
        self.health = 10
        self.max_health = 10
        self.aggressive = False
        self.attack_damage = 1

class Cow:
    def __init__(self) -> None:
        self.codename = "npc_cow"
        self.name = "Корова"
        self.health = 15
        self.max_health = 15
        self.aggressive = False
        self.attack_damage = 1

class Chicken:
    def __init__(self) -> None:
        self.codename = "npc_chicken"
        self.name = "Курица"
        self.health = 2
        self.max_health = 2
        self.aggressive = False
        self.attack_damage = 1

class Spider:
    def __init__(self) -> None:
        self.codename = "npc_spider"
        self.name = "Гиганский паук"
        self.health = 25
        self.max_health = 25
        self.aggressive = True
        self.attack_damage = 3

class Wolf:
    def __init__(self) -> None:
        self.codename = "npc_wolf"
        self.name = "Волк"
        self.health = 30
        self.max_health = 30
        self.aggressive = True
        self.attack_damage = 8


class Trader:
    def __init__(self) -> None:
        self.codename = "npc_trader"
        self.name = "Торговец"
        self.health = 150
        self.max_health = 150
        self.aggressive = False
        self.attack_damage = 1